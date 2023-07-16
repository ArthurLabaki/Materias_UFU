<?php

require "conexaoMysql.php";

class RequestResponse
{
    public $success;
    public $detail;

    function __construct($success, $detail)
    {
        $this->success = $success;
        $this->detail = $detail;
    }
}

$pdo = mysqlConnect();

$nome = $_POST["Nome"];
$cpf = $_POST["CPF"];
$cpf = str_replace(['.', '-'], '', $cpf);
$email = $_POST["Email"];
$senha = $_POST["Senha"];
$senhaHash = password_hash($senha, PASSWORD_DEFAULT);
$tel = $_POST["Telefone"];

try {
    // Verifica se os dados já existem no banco
    $stmt = $pdo->prepare("SELECT * FROM Anunciante WHERE CPF = ? OR Email = ?");
    $stmt->execute([$cpf, $email]);

    if ($stmt->rowCount() > 0) {
        // Dados já existem no banco
        $response = new RequestResponse(false, 'Email ou cpf já existe');
        echo json_encode($response);
        exit();
    }

    // Inicia a transação
    $pdo->beginTransaction();

    // Insere os dados na tabela Anunciante
    $stmt1 = $pdo->prepare("INSERT INTO Anunciante (Nome, CPF, Email, SenhaHash, Telefone) VALUES (?, ?, ?, ?, ?)");
    $stmt1->execute([$nome, $cpf, $email, $senhaHash, $tel]);

    // Confirma a transação
    $pdo->commit();

    $response = new RequestResponse(true, 'login.html');
    echo json_encode($response);

} catch (PDOException $e) {
    // Desfaz a transação em caso de erro
    $pdo->rollback();
    $response = new RequestResponse(false, 'Erro no servidor: ' . $e->getMessage());
    echo json_encode($response);
}

$pdo = null;
?>
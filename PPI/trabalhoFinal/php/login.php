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

function checkUserCredentials($pdo, $email, $senha)
{
    $sql = <<<SQL
    SELECT SenhaHash
    FROM Anunciante
    WHERE Email = ?
    SQL;

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([$email]);
        $senhaHash = $stmt->fetchColumn();

        if (!$senhaHash)
            return false; // a consulta não retornou nenhum resultado (email não encontrado)

        if (!password_verify($senha, $senhaHash))
            return false; // senha incorreta

        // email e senha corretos
        return true;
    } catch (Exception $e) {
        exit('Falha inesperada: ' . $e->getMessage());
    }
}

$email = $_POST['email'] ?? '';
$senha = $_POST['senha'] ?? '';

$pdo = mysqlConnect();
if (checkUserCredentials($pdo, $email, $senha)) {
    // cria uma nova sessão para o usuário
    session_start();
    $_SESSION['loggedIn'] = true;
    $_SESSION['user'] = $email;
    $response = new RequestResponse(true, 'php/home.php');
} else
    $response = new RequestResponse(false, ''); //$response = new RequestResponse(false, 'Erro no servidor: ' . $e->getMessage());

echo json_encode($response);

$pdo = null;
?>
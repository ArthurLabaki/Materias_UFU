<?php

require "../conexaoMysql.php";
$pdo = mysqlConnect();

$nome = $_POST["nome"];
$cpf = $_POST["cpf"];
$email = $_POST["email"];
$senha = $_POST["senha"];
$senhaHash = password_hash($senha, PASSWORD_DEFAULT);
$cep = $_POST["cep"];
$endereco = $_POST["endereco"];
$bairro = $_POST["bairro"];
$cidade = $_POST["cidade"];
$estado = $_POST["estado"];

try {
    // Inicia a transação
    $pdo->beginTransaction();

    // Insere os dados na tabela Cliente
    $stmt1 = $pdo->prepare("INSERT INTO Cliente (Nome, CPF, Email, Senha_hash) VALUES (?, ?, ?, ?)");
    $stmt1->execute([$nome, $cpf, $email, $senhaHash]);
    $cliente_id = $pdo->lastInsertId(); // Recupera o ID do último registro inserido

    // Insere os dados na tabela ClienteEndereco
    $stmt2 = $pdo->prepare("INSERT INTO ClienteEndereco (CEP, Endereco, Bairro, Cidade, Estado, cliente_codigo) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt2->execute([$cep, $endereco, $bairro, $cidade, $estado, $cliente_id]);

    // Confirma a transação
    $pdo->commit();

    header("location: listar.php");
} catch (PDOException $e) {
    // Desfaz a transação em caso de erro
    $pdo->rollback();

    echo "Erro ao inserir os dados: " . $e->getMessage();
}

?>
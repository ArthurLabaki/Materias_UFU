<?php

require "../conexaoMysql.php";
$pdo = mysqlConnect();

$nome = $_GET["nomeC"] ?? "";
$email = $_GET["emailC"] ?? "";
$mensagem = $_GET["infoC"] ?? "";

try {

    // código vulnerável a injeção de SQL
    $sql = <<<SQL
    INSERT INTO Contato (nome, email, mensagem)
    VALUES ('$nome', '$email', '$mensagem');
    SQL;

    $pdo->exec($sql);
    header("location: listaContato.php");

    exit();
} catch (Exception $e) {
    exit('Falha ao cadastrar os dados: ' . $e->getMessage());
}


?>
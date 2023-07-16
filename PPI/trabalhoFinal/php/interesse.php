<?php
require "conexaoMysql.php";
require "sessionVerification.php";

session_start();
exitWhenNotLoggedIn();

$pdo = mysqlConnect();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $dados = json_decode(file_get_contents("php://input"), true);
    // Dados enviados pelo formulário
    $mensagem = $dados["mensagem"];
    $contato = $dados["contato"];
    $codAnuncio = $dados["codAnuncio"];

    try {
        // Inserção dos dados na tabela "Interesse"
        $sql = "INSERT INTO Interesse (Mensagem, DataHora, Contato, CodAnuncio) VALUES (:mensagem, NOW(), :contato, :codAnuncio)";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(":mensagem", $mensagem);
        $stmt->bindParam(":contato", $contato);
        $stmt->bindParam(":codAnuncio", $codAnuncio); // Substitua pelo código do anúncio correspondente
        $stmt->execute();

        echo "Dados enviados com sucesso!";
    } catch (PDOException $e) {
        echo "Erro ao enviar os dados: " . $e->getMessage();
    }

}

$pdo = null;
?>
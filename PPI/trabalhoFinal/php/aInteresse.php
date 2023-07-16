<?php
require "conexaoMysql.php";

// Verifica se o código do interesse foi recebido
if (isset($_POST['codigoInteresse'])) {
    $codigoInteresse = $_POST['codigoInteresse'];

    $pdo = mysqlConnect();

    // Prepara e executa a query para apagar o interesse com base no código
    $sql = "DELETE FROM Interesse WHERE Codigo = :codigoInteresse";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':codigoInteresse', $codigoInteresse, PDO::PARAM_INT);
    $stmt->execute();

    // Verifica se o interesse foi apagado com sucesso
    if ($stmt->rowCount() > 0) {
        // Resposta de sucesso
        http_response_code(200);
        echo "Interesse apagado com sucesso!";
    } else {
        // Resposta de erro
        http_response_code(500);
        echo "Erro ao apagar o interesse.";
    }
} else {
    // Resposta de erro
    http_response_code(400);
    echo "Código do interesse não fornecido.";
}

$pdo = null;
?>
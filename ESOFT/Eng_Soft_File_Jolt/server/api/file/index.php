<?php
    header('Access-Control-Allow-Origin: *');

    $pdo = require '../../PGConnection.php';

    $arquivos = array();

    if (!array_key_exists("username", $_GET) || !array_key_exists("nome", $_GET)) {
        http_response_code(400);
        return;
    }

    $username = $_GET["username"] ?? "";
    $nome = $_GET["nome"] ?? "";

    $sql_time = <<<SQL
                SELECT a.*, u.nome as "user", u.username as username
                FROM arquivo a
                         JOIN usuario u on a.identificador = u.identificador
                where a.nome = :name and u.username = :user;
                SQL;

        //$stmt = $pdo->query($sql_time);
        $stmt = $pdo->prepare($sql_time);
        $stmt->bindParam(':name', $nome);
        $stmt->bindParam(':user', $username);
        $stmt->execute();

        while($row = $stmt->fetch()){
            $arquivos[] = $row;
        }

    header('Content-type: application/json');
    echo json_encode($arquivos);
?>
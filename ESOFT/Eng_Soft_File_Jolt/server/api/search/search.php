<?php
    header('Access-Control-Allow-Origin: *');

    $pdo = require '../../PGConnection.php';

    $arquivos = array();

    $text = $_GET["text"] ?? "";
    $pattern = '%' . $text . '%';


    $sql = <<<SQL
                SELECT * FROM arquivo
                WHERE titulo LIKE :pattern
                ORDER BY data DESC;
                SQL;

    if($text != ""){
        $stmt = $pdo->prepare($sql);
        $stmt->execute([':pattern' => $pattern]);

        while($row = $stmt->fetch()){
            $arquivos[] = $row;
        }

    } else{
        $arquivos[] = "Input Error!";
    }



    header('Content-type: application/json');
    echo json_encode($arquivos);
?>
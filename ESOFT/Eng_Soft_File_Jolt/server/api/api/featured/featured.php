<?php
    header('Access-Control-Allow-Origin: *');

    $pdo = require '../../PGConnection.php';

    $arquivos = array();

    $type = $_GET["feature-type"] ?? "";

    $sql_time = <<<SQL
                SELECT * FROM arquivo
                ORDER BY data DESC;
                SQL;

    $sql_downloads = <<<SQL
                    SELECT * FROM arquivo
                    ORDER BY qtd_downloads DESC;
                    SQL;

    $sql_votes = <<<SQL
                SELECT *
                FROM avalia AV JOIN (arquivo AR JOIN usuario US ON 
                    US.identificador = AR.identificador)ON
                    AR.identificador = AV.identificador_criador
                ORDER BY nota DESC;
                SQL;

    if($type == "time"){
        $stmt = $pdo->query($sql_time);

        while($row = $stmt->fetch()){
            $arquivos[] = $row;
        }

    } else if($type == "downloads"){
        $stmt = $pdo->query($sql_downloads);

        while($row = $stmt->fetch()){
            $arquivos[] = $row;
        }

    } else if($type == "votes"){
        $stmt = $pdo->query($sql_votes);

        while($row = $stmt->fetch()){
            $arquivos[] = $row;
        }

    } else{
        $arquivos[] = "Input Error!";
    }



    header('Content-type: application/json');
    echo json_encode($arquivos);
?>
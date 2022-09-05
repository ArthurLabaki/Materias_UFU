<?php
    header('Access-Control-Allow-Origin: *');

    $pdo = require '../../PGConnection.php';

    $arquivos = array();

    $type = $_GET["feature-type"] ?? "";

    $sql_time = <<<SQL
                SELECT a.*, u.nome as user, u.username as username
                FROM arquivo a JOIN usuario u on a.identificador = u.identificador
                ORDER BY a.data DESC;
                SQL;

    $sql_downloads = <<<SQL
                    SELECT a.*, u.nome as user, u.username as username
                    FROM arquivo a JOIN usuario u on a.identificador = u.identificador
                    ORDER BY a.qtd_downloads DESC;
                    SQL;

    $sql_votes = <<<SQL
                SELECT AR.*, US.nome as user, US.username as username
                FROM avalia AV
                         JOIN (arquivo AR JOIN usuario US ON
                    US.identificador = AR.identificador) ON
                    AR.identificador = AV.identificador_criador
                ORDER BY AV.nota DESC;
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
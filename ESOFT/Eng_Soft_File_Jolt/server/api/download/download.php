<?php
    //var/filebank/joao/livro1/0.1/livro.pdf
    header('Access-Control-Allow-Origin: *');

    $pdo = require '../../PGConnection.php';

    $target_dir = "/var/filebank/";

    $arquivos = array();

    if (!array_key_exists("username", $_GET) || !array_key_exists("nome", $_GET)) {
        http_response_code(400);
        return;
    }

    $username = $_GET["username"] ?? "";
    $nome = $_GET["nome"] ?? "";
    $qtd_downloads = 0;

    // Checking whether file exists or not
    if (file_exists($target_dir . $username . '/' . $nome)) {
        $target_dir = $target_dir . $username . '/' . $nome;
        $arquivos[] = $target_dir;
        $arquivos[] =  "Given file path exists";
    }
    else {
        $arquivos[] =  "The Given file path does not exists";
        return;
    }

    for ($i = 10; $i >= 1; $i--) {
        if(file_exists($target_dir . '/' . $i)){
            $target_dir = $target_dir . '/' . $i;
            $arquivos[] = $target_dir;
            $arquivos[] =  "Given file version path exists. Version: " . $i;
            break;

        }
        
        if($i == 1){
            $arquivos[] =  "There is no existent version path.";
        }
    }

    $files = glob($target_dir.'/*'); 
    foreach($files as $file) {

        if (file_exists($file)) {

            header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
            header("Cache-Control: public"); // needed for internet explorer
            //header("Content-Type: application/zip");
            header("Content-Transfer-Encoding: Binary");
            header("Content-Length:".filesize($file));
            header('Content-Disposition: attachment; filename="' . basename($file) . '"');
            readfile($file);
            die();        
        } else {
            die("Error: File not found.");
        }
    }

    /*$attachment_location = $target_dir . "/*";
    if (file_exists($attachment_location)) {

        header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
        header("Cache-Control: public"); // needed for internet explorer
        //header("Content-Type: application/zip");
        header("Content-Transfer-Encoding: Binary");
        header("Content-Length:".filesize($attachment_location));
        header("Content-Disposition: attachment;");
        readfile($attachment_location);
        die();        
    } else {
        die("Error: File not found.");
    }*/

    /*if ($username != "" && $file != ""){
        fopen($target_dir . $username . '/' . basename($file),mode)
    }
    else{
    }*/

    /*$sql_time = <<<SQL
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
    }*/



    header('Content-type: application/json');
    echo json_encode($arquivos);
?>
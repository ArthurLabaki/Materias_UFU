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

    $files = glob($target_dir.'/capa/*'); 
    foreach($files as $file) {

        if (file_exists($file)) {

            header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
            header("Cache-Control: public"); // needed for internet explorer
            header("Content-Type: image/png");
            //header("Content-Transfer-Encoding: Binary");
            header("Content-Length:".filesize($file));
            //header('Content-Disposition: attachment; filename="' . basename($file) . '"');
            readfile($file);
            die();        
        } else {
            die("Error: File not found.");
        }
    }

    header('Content-type: application/json');
    echo json_encode($arquivos);
?>
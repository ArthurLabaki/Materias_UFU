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
    //$file = $_GET["file"] ?? "";
    $nome = $_GET["nome"] ?? "";
    /*$descricao = $_GET["descricao"] ?? "";
    $titulo = $_GET["titulo"] ?? "";
    $qtd_downloads = 0;*/

    // Checking whether file exists or not
    if (!file_exists($target_dir . $username . '/' . $nome)) {
    
        // Create a new file or direcotry
        try {
            mkdir($target_dir . $username . '/' . $nome, 0777, true);
        } catch(ErrorException $ex) {
            echo "Error: " . $ex->getMessage();
            return;
        }        

        $target_dir = $target_dir . $username . '/' . $nome;
        $arquivos[] = $target_dir;
        $arquivos[] =  "Given file path successfully created";
    }
    else {
        $target_dir = $target_dir . $username . '/' . $nome;
        $arquivos[] = $target_dir;
        $arquivos[] =  "The Given file path already exists";
    }

    for ($i = 1; $i <= 10; $i++) {
        if(!file_exists($target_dir . '/' . $i)){

            // Create a new file or direcotry
            try {
                mkdir($target_dir . '/' . $i, 0777, true);
            } catch(ErrorException $ex) {
                echo "Error: " . $ex->getMessage();
                return;
            }

            $target_dir = $target_dir . '/' . $i;
            $arquivos[] = $target_dir;
            $arquivos[] =  "Given file version path successfully created. Version: " . $i;
            break;
        }else if($i == 10){
            $files = glob($target_dir.'/1/*'); 
   
            // Deleting all the files in the list
            foreach($files as $file) {
            
                if(is_file($file)) 
                
                    // Delete the given file
                    unlink($file);
            }

            // removing directory using rmdir()
            if(rmdir($target_dir.'/1'))
            {
                $arquivos[] = $target_dir . "/1 successfully removed";
            }
            else
            {
                $arquivos[] = $target_dir.'/1' . "couldn't be removed"; 
            }

            for ($j = 1; $j <= 9; $j++) {
                rename($target_dir.'/'.$j, $target_dir.'/'.($j+1));
                $arquivos[] =  "File " . $target_dir . '/' . ($j+1) . " was renamed to " . $target_dir . '/' . $j;
            }
            
            $i = 9;
        }
    }

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
<?php
    //require_once "PGConnection.php";
    $pdo = require 'PGConnection.php';

    $sql = <<<SQL
    SELECT nome
    FROM usuario
    SQL;

    $stmt = $pdo->query($sql);
    $users = array();

    while($row = $stmt->fetch()){
        $users[] = $row;
    }

    header('Content-type: application/json');
    echo json_encode($users);

    /*<?php
    // Your code here!
        $users = array();
        $count = 0;
        
        echo $count;
        
        while($count < 10){
            echo $count;
            $users[] = $count;
            $count++;
        }
        
        $json = json_encode($users);
        echo $json;
        return $json;
        
        /*$count = 0;
        while($count < 0){
            echo $users[$count];
            $count++;
    }*/
?>

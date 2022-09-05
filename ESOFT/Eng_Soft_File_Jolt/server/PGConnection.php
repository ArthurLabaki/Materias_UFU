<?php

    require_once '/var/www/secrets.php';

    function connect(string $host, string $db, string $user, string $port, string $password): PDO
    {
        try {
            $dsn = "pgsql:host=$host;port=$port;dbname=$db";

            $options = [
                PDO::ATTR_EMULATE_PREPARES => false, // desativa a execução emulada de prepared statements
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // ativa o modo de erros para lançar exceções    
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // altera o modo padrão do método fetch para FETCH_ASSOC
            ];

            // make a database connection
            $Conn = new PDO(
                $dsn,
                $user,
                $password,
                $options
            );


            return $Conn;
        } catch (PDOException $e) {
            die($e->getMessage());
        }
    }

    return connect($host, $db, $user, $port, $password);
?>

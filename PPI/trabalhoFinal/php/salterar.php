<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();
session_start();

$pdo = mysqlConnect();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_SESSION['user'];
    $fieldsToUpdate = [];

    if (!empty($_POST["nome"])) {
        $fieldsToUpdate['Nome'] = $_POST["nome"];
    }

    if (!empty($_POST["telefone"])) {
        $fieldsToUpdate['Telefone'] = $_POST["telefone"];
    }

    if (!empty($_POST["senha"])) {
        $fieldsToUpdate['SenhaHash'] = password_hash($_POST["senha"], PASSWORD_DEFAULT);
    }

    if (count($fieldsToUpdate) > 0) {
        $placeholders = implode(',', array_map(function ($field) {
            return $field . '=:' . $field;
        }, array_keys($fieldsToUpdate)));

        try {
            $sql = "UPDATE Anunciante SET {$placeholders} WHERE Email=:email";
            $stmt = $pdo->prepare($sql);
            $stmt->bindParam(':email', $email);

            foreach ($fieldsToUpdate as $field => $value) {
                $stmt->bindParam(':' . $field, $value);
            }

            $stmt->execute();

            header("Location: home.php"); // Redireciona para home.php
            exit();
        } catch (PDOException $e) {
            echo "Erro ao atualizar valores no banco de dados: " . $e->getMessage();
        }
    }
}

$pdo = null;
?>
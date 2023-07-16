<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();

$stmt = $pdo->prepare("SELECT Codigo, Nome, Descricao FROM Categoria");
$stmt->execute();

$categorias = array();

if ($stmt->rowCount() > 0) {
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $categoria = array(
            'Codigo' => $row['Codigo'],
            'Nome' => $row['Nome'],
            'Descricao' => $row['Descricao']
        );
        $categorias[] = $categoria;
    }
} else {
    // Tratar o caso em que nenhuma categoria foi encontrada
    echo json_encode(array('error' => 'Nenhuma categoria encontrada'));
    exit;
}

header('Content-type: application/json');
echo json_encode($categorias);

$pdo = null;
?>
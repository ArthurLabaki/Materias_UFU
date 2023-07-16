<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();

$inputData = json_decode(file_get_contents('php://input'), true);
$keyword = $inputData['query'];
$keywords = explode(' ', $keyword);
$palavrasChave = array_slice($keywords, 0, 5);

$searchField = $inputData['searchField'];
$minPrice = $inputData['minPrice'];
$maxPrice = $inputData['maxPrice'];
$categories = $inputData['categories'];
$whereClause = '';

foreach ($palavrasChave as $index => $palavraChave) {
    $param = ":palavraChave$index";
    $whereClause .= "$searchField LIKE CONCAT('%', $param, '%') AND ";
}

if (!empty($minPrice) && !empty($maxPrice)) {
    $whereClause .= "Preco BETWEEN :minPrice AND :maxPrice AND ";
}

if (!empty($categories)) {
    $whereClause .= "CodCategoria IN (" . implode(",", $categories) . ") AND ";
}

$whereClause = rtrim($whereClause, "AND ");

$sql = "SELECT * FROM Anuncio WHERE $whereClause";
$stmt = $pdo->prepare($sql);

foreach ($palavrasChave as $index => $palavraChave) {
    $param = ":palavraChave$index";
    $stmt->bindValue($param, "%$palavraChave%", PDO::PARAM_STR);
}

if (!empty($minPrice) && !empty($maxPrice)) {
    $stmt->bindValue(':minPrice', $minPrice, PDO::PARAM_STR);
    $stmt->bindValue(':maxPrice', $maxPrice, PDO::PARAM_STR);
}

$stmt->execute();

if ($stmt->rowCount() > 0) {
    // Exibe os anúncios encontrados
    echo '<h1 id="teste">Anúncios encontrados!</h1>';
    echo '<hr>';
    echo '<section class="card-sec">';

    $count = 0; // Contador de itens exibidos

    while ($row = $stmt->fetch()) {
        if ($count >= 6) {
            break; // Sai do loop quando exibir 6 itens
        }

        $codigoAnuncio = $row["Codigo"];
        $titulo = $row["Titulo"];
        $preco = $row["Preco"];
        $descricao = $row["Descricao"];

        // Consulta a tabela Foto para obter o nome do arquivo de imagem
        $sqlFoto = "SELECT NomeArqFoto FROM Foto WHERE CodAnuncio = :codigoAnuncio LIMIT 1";
        $stmtFoto = $pdo->prepare($sqlFoto);
        $stmtFoto->bindParam(':codigoAnuncio', $codigoAnuncio);
        $stmtFoto->execute();
        $foto = $stmtFoto->fetch(PDO::FETCH_ASSOC);
        $imagem = $foto ? $foto['NomeArqFoto'] : 'nome_da_imagem_padrao.jpg';

        echo '<div class="card">';
        echo "<a href=\"produto.php?codigo=$codigoAnuncio\">";
        echo "<h2>$titulo</h2>";
        echo "<h3>R$ $preco</h3>";
        echo "<img src=\"../img/server/$imagem\" alt=\"Imagem\">";
        echo "<p>" . substr($descricao, 0, 200) . "...</p>";
        echo "</a>";
        echo '</div>';

        $count++;
    }

    echo '</section>';
} else {
    echo "Nenhum anúncio encontrado.";
}

// Fecha a conexão com o banco de dados
$pdo = null;

?>
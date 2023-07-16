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
$page = $inputData['page']; // Número da página solicitada
$resultsPerPage = 6; // Número de resultados por página

$offset = ($page - 1) * $resultsPerPage; // Calcula o deslocamento
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

$sql = "SELECT * FROM Anuncio WHERE $whereClause ORDER BY DataHora DESC LIMIT $resultsPerPage OFFSET $offset";
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

$response = []; // Array para armazenar a resposta

if ($stmt->rowCount() > 0) {
    $response['status'] = 'success';
    $response['message'] = 'Anúncios encontrados!';
    $response['data'] = [];


    while ($row = $stmt->fetch()) {

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

        $item = [
            'codigoAnuncio' => $codigoAnuncio,
            'titulo' => $titulo,
            'preco' => number_format($preco, 2, ',', '.'),
            'imagem' => $imagem,
            'descricao' => substr($descricao, 0, 200) . "..."
        ];

        $response['data'][] = $item;
    }
} else {
    $response['status'] = 'error';
    $response['message'] = 'Nenhum anúncio encontrado.';
}


header('Content-Type: application/json');
echo json_encode($response);

$pdo = null;
?>
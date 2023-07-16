<?php

require "conexaoMysql.php";
require "sessionVerification.php";

session_start();
exitWhenNotLoggedIn();
class RequestResponse
{
    public $success;
    public $detail;

    function __construct($success, $detail)
    {
        $this->success = $success;
        $this->detail = $detail;
    }
}

$pdo = mysqlConnect();

$tit = $_POST["titulo"];
$val = $_POST["val"];
$cep = $_POST["cep"];
$bar = $_POST["bar"];
$city = $_POST["city"];
$est = $_POST["est"];
$desc = $_POST["desc"];
$cat = $_POST["cat"];
$dataHora = date('Y-m-d H:i:s');
$email = $_SESSION['user'];

try {
    // Pega o código do anunciante
    $stmt = $pdo->prepare("SELECT Codigo FROM Anunciante WHERE Email = ?");
    $stmt->execute([$email]);
    $codigoAnun = $stmt->fetchColumn();

    // Busca o código da categoria com base no nome da categoria fornecido
    $stmt1 = $pdo->prepare("SELECT Codigo FROM Categoria WHERE Nome = ?");
    $stmt1->execute([$cat]);
    $codigoCat = $stmt1->fetchColumn();

    if (!$codigoCat) {
        // Categoria não encontrada
        $response = new RequestResponse(false, 'Categoria não encontrada');
        echo json_encode($response);
        exit();
    }

    // Inicia a transação
    $pdo->beginTransaction();

    // Insere os dados na tabela Anuncio
    $stmt2 = $pdo->prepare("INSERT INTO Anuncio (Titulo, Descricao, Preco, DataHora, CEP, Bairro, Cidade, Estado, CodCategoria, CodAnunciante) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt2->execute([$tit, $desc, $val, $dataHora, $cep, $bar, $city, $est, $codigoCat, $codigoAnun]);

    // Recupera o código do anúncio inserido
    $codigoAnuncio = $pdo->lastInsertId();

    // Salva as imagens
    $imagens = $_FILES['imagens'];
    $numImagens = count($imagens['name']);

    for ($i = 0; $i < $numImagens; $i++) {
        $nomeTemporario = $imagens['tmp_name'][$i];
        $extensao = pathinfo($imagens['name'][$i], PATHINFO_EXTENSION);
        $prefixo = 'imagem_' . time(); // Prefixo para garantir um nome exclusivo
        $nomeArquivo = $prefixo . '_' . $i . '.' . $extensao;
        $caminhoDestino = '../img/server/' . $nomeArquivo;

        if (move_uploaded_file($nomeTemporario, $caminhoDestino)) {
            // Insere o nome do arquivo na tabela Foto
            $stmt3 = $pdo->prepare("INSERT INTO Foto (CodAnuncio, NomeArqFoto) VALUES (?, ?)");
            $stmt3->execute([$codigoAnuncio, $nomeArquivo]);
        }
    }



    // Confirma a transação
    $pdo->commit();

    $response = new RequestResponse(true, 'lAnuncio.php');
    echo json_encode($response);

} catch (PDOException $e) {
    // Desfaz a transação em caso de erro
    $pdo->rollback();
    $response = new RequestResponse(false, 'Erro no servidor: ' . $e->getMessage());
    echo json_encode($response);
}

$pdo = null;
?>
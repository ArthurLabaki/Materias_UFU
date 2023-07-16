<?php
require "conexaoMysql.php";
require "sessionVerification.php";

session_start();
exitWhenNotLoggedIn();

$pdo = mysqlConnect();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $titulo = $_POST["titulo"];

    // Verifica se o título foi fornecido
    if (empty($titulo)) {
        $response = [
            "success" => false,
            "detail" => "O campo de título é obrigatório."
        ];
        echo json_encode($response);
        exit();
    }

    // Busca o anúncio no banco de dados pelo título
    $sql = "SELECT Codigo, CodAnunciante FROM Anuncio WHERE Titulo = :titulo";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":titulo", $titulo);
    $stmt->execute();
    $anuncio = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verifica se o anúncio foi encontrado
    if (!$anuncio) {
        $response = [
            "success" => false,
            "detail" => "Anúncio não encontrado."
        ];
        echo json_encode($response);
        exit();
    }

    $codigoAnuncio = $anuncio["Codigo"];
    $codAnuncianteAnuncio = $anuncio["CodAnunciante"];

    // Obtém o código do anunciante logado com base no email da sessão
    $email = $_SESSION['user'];
    $stmtAnunciante = $pdo->prepare("SELECT Codigo FROM Anunciante WHERE Email = ?");
    $stmtAnunciante->execute([$email]);
    $codigoAnun = $stmtAnunciante->fetchColumn();

    // Verifica se o anunciante é o proprietário do anúncio a ser excluído
    if ($codigoAnun != $codAnuncianteAnuncio) {
        $response = [
            "success" => false,
            "detail" => "Você não tem permissão para excluir este anúncio."
        ];
        echo json_encode($response);
        exit();
    }

    try {
        $pdo->beginTransaction();

        // Busca os nomes das fotos do anúncio a serem excluídas
        $sqlSelectFotos = "SELECT NomeArqFoto FROM Foto WHERE CodAnuncio = :codigoAnuncio";
        $stmtSelectFotos = $pdo->prepare($sqlSelectFotos);
        $stmtSelectFotos->bindParam(":codigoAnuncio", $codigoAnuncio);
        $stmtSelectFotos->execute();
        $fotos = $stmtSelectFotos->fetchAll(PDO::FETCH_ASSOC);

        // Exclui as imagens do banco de dados
        foreach ($fotos as $foto) {
            $nomeArquivo = $foto["NomeArqFoto"];
            $caminhoDestino = "../img/server/" . $nomeArquivo;
            unlink($caminhoDestino);
        }

        // Exclui as fotos do anúncio da tabela Foto
        $sqlDeleteFotos = "DELETE FROM Foto WHERE CodAnuncio = :codigoAnuncio";
        $stmtDeleteFotos = $pdo->prepare($sqlDeleteFotos);
        $stmtDeleteFotos->bindParam(":codigoAnuncio", $codigoAnuncio);
        $stmtDeleteFotos->execute();

        // Exclui as fotos do anúncio da tabela Interesse
        $sqlDeleteInteresse = "DELETE FROM Interesse WHERE CodAnuncio = :codigoAnuncio";
        $stmtDeleteInteresse = $pdo->prepare($sqlDeleteInteresse);
        $stmtDeleteInteresse->bindParam(":codigoAnuncio", $codigoAnuncio);
        $stmtDeleteInteresse->execute();

        // Exclui o anúncio da tabela Anuncio
        $sqlDeleteAnuncio = "DELETE FROM Anuncio WHERE Codigo = :codigoAnuncio";
        $stmtDeleteAnuncio = $pdo->prepare($sqlDeleteAnuncio);
        $stmtDeleteAnuncio->bindParam(":codigoAnuncio", $codigoAnuncio);
        $stmtDeleteAnuncio->execute();

        $pdo->commit();

        $response = [
            "success" => true,
            "detail" => "lAnuncio.php"
        ];
        echo json_encode($response);
    } catch (PDOException $e) {
        $pdo->rollBack();
        $response = [
            "success" => false,
            "detail" => "Erro ao excluir o anúncio: " . $e->getMessage()
        ];
        echo json_encode($response);
    }
} else {
    // Responde com erro caso a requisição não seja do tipo POST
    $response = [
        "success" => false,
        "detail" => "Método de requisição inválido."
    ];
    echo json_encode($response);
}

$pdo = null;
?>
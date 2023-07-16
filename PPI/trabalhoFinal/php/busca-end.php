<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();

class Endereco
{
    public $bairro;
    public $cidade;
    public $estado;

    function __construct($bairro, $cidade, $estado)
    {
        $this->bairro = $bairro;
        $this->cidade = $cidade;
        $this->estado = $estado;
    }
}

$cep = $_GET['cep'] ?? '';
$sql = "SELECT Bairro, Cidade, Estado FROM BaseEnderecosAjax WHERE CEP = :cep";

try {
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(':cep' => $cep));
    if ($stmt->rowCount() > 0) {
        $dados = $stmt->fetch(PDO::FETCH_ASSOC);
        $endereco = new Endereco($dados['Bairro'], $dados['Cidade'], $dados['Estado']);
    } else {
        $endereco = new Endereco('', '', '');
    }
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($endereco);
} catch (PDOException $e) {
    die('Erro ao buscar endereço no banco de dados: ' . $e->getMessage());
}

$pdo = null;
?>
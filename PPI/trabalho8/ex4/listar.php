<?php

require "../conexaoMysql.php";
$pdo = mysqlConnect();

// Recupera todos os dados cadastrados nas duas tabelas
$stmt = $pdo->prepare("SELECT c.Nome, c.CPF, c.Email, ce.Endereco, ce.Bairro, ce.Cidade, ce.Estado 
                           FROM Cliente c JOIN ClienteEndereco ce ON c.codigo = ce.cliente_codigo");
$stmt->execute();
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Listagem de Clientes</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        thead {
            background-color: #ddd;
        }

        th {
            font-weight: bold;
            text-align: left;
            padding: 8px;
        }

        td {
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }

        tbody tr:hover {
            background-color: #f5f5f5;
        }
    </style>
</head>

<body>
    <h1>Listagem de Clientes</h1>

    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>CPF</th>
                <th>E-mail</th>
                <th>Endereço</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>Estado</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($rows as $row): ?>
                <tr>
                    <td>
                        <?= htmlspecialchars($row["Nome"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["CPF"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["Email"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["Endereco"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["Bairro"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["Cidade"]) ?>
                    </td>
                    <td>
                        <?= htmlspecialchars($row["Estado"]) ?>
                    </td>
                </tr>
            <?php endforeach ?>
        </tbody>
    </table>
</body>

</html>
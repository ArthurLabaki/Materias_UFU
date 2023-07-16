<html>

<head>
    <title>Dados do Contato</title>
</head>

<body>
    <h1>Dados do Contato</h1>
    <table>
        <tr>
            <th>Campo</th>
            <th>Valor</th>
        </tr>
        <tr>
            <td>Nome:</td>
            <td>
                <?php echo $_GET['nomeC']; ?>
            </td>
        </tr>
        <tr>
            <td>E-mail:</td>
            <td>
                <?php echo $_GET['emailC']; ?>
            </td>
        </tr>
        <tr>
            <td>Mensagem:</td>
            <td>
                <?php echo $_GET['infoC']; ?>
            </td>
        </tr>
    </table>
</body>

</html>
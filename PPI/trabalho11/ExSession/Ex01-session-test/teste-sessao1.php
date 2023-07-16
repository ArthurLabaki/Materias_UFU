<?php

// inicializa a sessão
session_start();

// nome e e-mail recebidos de formulário
$nome = $_POST['nome'] ?? '';
$email = $_POST['email'] ?? '';

// armazena os valores em variáveis de sessão
$_SESSION['nome']  = $nome;
$_SESSION['email'] = $email;

?>
<!DOCTYPE html>
<html><body>
  <h2>Variáveis de sessão definidas!</h2>
  <h3>
    <a href="teste-sessao2.php">
      Acessar outro script PHP
    </a>
  </h3>
</body></html>


<?php

require "php/conexaoMysql.php";

$pdo = mysqlConnect();

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="description"
        content="Transforme seus negócios em uma experiência incrivelmente fácil e rápida com o CrowSpot, o portal de anúncios definitivo para compras e vendas na web!">
    <link rel="stylesheet" href="css/style.css">
    <script src="js/script.js"></script>
    <title> CrowSpot - Home </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        hr {
            color: black;
            border-width: 2px;
            border-style: dashed;
            margin-top: 15px;
            margin-bottom: 25px;
            width: 100%;
        }

        main a {
            text-decoration: none;
            color: black;
            padding: 0;
            margin: 0;
        }

        main .card-sec {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            text-align: center;
            margin: 5px 0;
        }

        main .card-sec .card {
            border: 3px dashed black;
            min-width: 300px;
            min-height: 350px;
            width: 30%;
            height: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 5px 15px 30px 15px;
            overflow: hidden;
        }

        main .card-sec .card img {
            width: 200px;
            height: 200px;
            border: 2px solid black;

        }

        main .card-sec .card h2 {
            text-align: center;
            font-style: italic;
            margin: 10px 15px;
        }

        main .card-sec .card h3 {
            color: darkgreen;
            font-weight: bold;
            text-align: center;
            margin: 0px 15px 10px 15px;
        }

        main .card-sec .card p {
            text-align: justify;
            font-size: medium;
            margin: 15px;
        }
    </style>
</head>

<body>
    <header>
        <a href="index.html">
            <img src="img/Logo_CrowSpot.png" alt="CrowSpot - portal de anúncios">
        </a>
        <a href="login.html" class="button">Login</a>
    </header>
    <nav>
        <form id="searchForm">
            <div id="divBusca">
                <input type="text" id="inpBusca" placeholder="Buscar...">
                <button id="btnExp" type="button" title="Opções avançadas">
                    <img src="img/expand.png" class="imgBtn" alt="Expandir">
                </button>
                <button id="btnBusca" type="submit" title="Buscar">
                    <img src="img/lupa.png" class="imgBtn" alt="Buscar">
                </button>
            </div>
        </form>
        <script>
            document.getElementById('searchForm').addEventListener('submit', function (event) {
                event.preventDefault(); // Impede o envio padrão do formulário
                var mainElement = document.querySelector('main');
                mainElement.innerHTML = '';

                var query = document.getElementById('inpBusca').value;
                var searchField = getSearchField();
                var minPrice = document.getElementById('inpMin').value;
                var maxPrice = document.getElementById('inpMax').value;
                var categories = getSelectedCategories();
                var currentPage = 1; // Página inicial

                function loadResults(page) {
                    fetch('php/buscaProduto.php', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            query: query,
                            searchField: searchField,
                            minPrice: minPrice,
                            maxPrice: maxPrice,
                            categories: categories,
                            page: page,
                        }),
                    })
                        .then(function (response) {
                            if (!response.ok) {
                                throw new Error('Erro na busca');
                            }
                            return response.json();
                        })
                        .then(function (data) {
                            var mainElement = document.querySelector('main');

                            if (data.status === 'success') {
                                var sectionElement = document.createElement('section');
                                sectionElement.classList.add('card-sec');

                                data.data.forEach(function (item) {
                                    var divElement = document.createElement('div');
                                    divElement.classList.add('card');

                                    var aElement = document.createElement('a');
                                    aElement.href = 'produto.php?codigo=' + item.codigoAnuncio;

                                    var h2Element = document.createElement('h2');
                                    h2Element.textContent = item.titulo;
                                    aElement.appendChild(h2Element);

                                    var h3Element = document.createElement('h3');
                                    h3Element.textContent = 'R$ ' + item.preco;
                                    aElement.appendChild(h3Element);

                                    var imgElement = document.createElement('img');
                                    imgElement.src = 'img/server/' + item.imagem;
                                    imgElement.alt = 'Imagem';
                                    aElement.appendChild(imgElement);

                                    var pElement = document.createElement('p');
                                    pElement.textContent = item.descricao;
                                    aElement.appendChild(pElement);

                                    divElement.appendChild(aElement);
                                    sectionElement.appendChild(divElement);
                                });

                                mainElement.appendChild(sectionElement);
                            }
                        })
                        .catch(function (error) {
                            alert(error.message);
                        });
                }

                // Função para verificar se o usuário chegou ao final da página
                function checkScroll() {
                    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
                        currentPage++; // Incrementa o número da página
                        loadResults(currentPage); // Carrega mais resultados
                    }
                }

                // Executa a primeira busca
                loadResults(currentPage);

                // Adiciona o event listener de scroll
                window.addEventListener('scroll', checkScroll);
            });


            function getSearchField() {
                var tituloChecked = document.getElementById('titulo').checked;
                var descricaoChecked = document.getElementById('descricao').checked;

                if (tituloChecked) {
                    return 'Titulo';
                } else if (descricaoChecked) {
                    return 'Descricao';
                }

                return ''; // Retorna vazio se nenhum campo estiver selecionado
            }
            function getSelectedCategories() {
                var checkboxes = document.querySelectorAll('#categorias input[type="checkbox"]:checked');
                var selectedCategories = [];

                checkboxes.forEach(function (checkbox) {
                    selectedCategories.push(checkbox.value);
                });
                return selectedCategories;
            }

        </script>
        <div class="modal">
            <div class="modalContent">
                <h2>Filtro de busca avançado</h2>
                <fieldset>
                    <legend>Buscar no:</legend>
                    <div class="checkbox">
                        <input type="checkbox" id="titulo" name="titulo" checked
                            onclick="manterUmCheckboxMarcado('titulo', 'descricao')">
                        <label for="titulo">Título</label>
                    </div>
                    <div class="checkbox">
                        <input type="checkbox" id="descricao" name="descricao"
                            onclick="manterUmCheckboxMarcado('descricao', 'titulo')">
                        <label for="descricao">Descrição</label>
                    </div>
                </fieldset>
                <script>
                    function manterUmCheckboxMarcado(id, outroId) {
                        const checkbox = document.getElementById(id);
                        const outroCheckbox = document.getElementById(outroId);

                        if (checkbox.checked) {
                            outroCheckbox.checked = false;
                        } else {
                            outroCheckbox.checked = true;
                        }
                    }
                </script>
                <fieldset>
                    <legend>Faixa de preço:</legend>
                    <div class="preco">
                        <input type="number" id="inpMin" placeholder="Valor mínimo..." min="0">
                    </div>
                    <div class="preco">
                        <input type="number" id="inpMax" placeholder="Valor máximo..." min="0">
                    </div>
                </fieldset>
                <fieldset id="categorias">
                    <legend>Categorias:</legend>
                </fieldset>
                <button class="btnClose">Salvar</button>
            </div>
        </div>
    </nav>
    <script>
        // Função para obter e adicionar categorias à janela modal
        function adicionarCategoriasModal() {
            fetch("php/categorias.php")
                .then(response => response.json())
                .then(data => {
                    // Selecionar o elemento fieldset de categorias na janela modal
                    const fieldsetCategorias = document.querySelector('fieldset#categorias');

                    // Limpar as opções de categoria existentes
                    fieldsetCategorias.innerHTML = '';

                    // Iterar sobre as categorias e adicionar as opções dinamicamente
                    data.forEach(categoria => {
                        const checkbox = document.createElement('div');
                        checkbox.classList.add('checkbox');

                        const input = document.createElement('input');
                        input.type = 'checkbox';
                        input.id = categoria.Nome ? categoria.Nome.toLowerCase().replace(/ /g, '-') : '';
                        input.name = 'categoria';
                        input.value = categoria.Codigo; // Definir o valor como o código da categoria

                        const label = document.createElement('label');
                        label.htmlFor = input.id;
                        label.textContent = categoria.Nome;

                        checkbox.appendChild(input);
                        checkbox.appendChild(label);

                        fieldsetCategorias.appendChild(checkbox);
                    });
                })
                .catch(error => {
                    console.log("Erro ao obter categorias: " + error);
                });
        }

        // Chamar a função ao clicar no botão de expansão
        const btnExp = document.getElementById('btnExp');
        btnExp.addEventListener('click', adicionarCategoriasModal);

    </script>

    <main>
        <h1 id="teste">CrowSpot, anunciar seus produtos nunca foi tão fácil!</h1>
        <hr>
        <h2>Anúncios em destaque</h2>
        <section class="card-sec">
            <?php
            // Faz a consulta no banco de dados para obter 3 anúncios aleatórios
            $sql = "SELECT * FROM Anuncio ORDER BY RAND() LIMIT 3";
            $stmt = $pdo->prepare($sql);
            $stmt->execute();
            $resultado = $stmt->fetchAll(PDO::FETCH_ASSOC);



            foreach ($resultado as $row) {
                $codigoAnuncio = $row['Codigo'];
                $titulo = $row['Titulo'];
                $descricao = $row['Descricao'];
                $preco = $row['Preco'];
                $preco = number_format($preco, 2, ',', '.');

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
                echo "<img src=\"img/server/$imagem\" alt=\"Imagem\">";
                echo "<p>" . substr($descricao, 0, 200) . "...</p>";
                echo "</a>";
                echo '</div>';
            }
            ?>
        </section>

        <hr>
        <h2>Novos anúncios</h2>
        <section class="card-sec">
            <?php
            // Faz a consulta no banco de dados para obter os 3 anúncios mais recentes
            $sql = "SELECT * FROM Anuncio ORDER BY DataHora DESC LIMIT 3";
            $stmt = $pdo->prepare($sql);
            $stmt->execute();
            $resultado = $stmt->fetchAll(PDO::FETCH_ASSOC);

            foreach ($resultado as $row) {
                $codigoAnuncio = $row['Codigo'];
                $titulo = $row['Titulo'];
                $descricao = $row['Descricao'];
                $preco = $row['Preco'];
                $preco = number_format($preco, 2, ',', '.');

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
                echo "<img src=\"img/server/$imagem\" alt=\"Imagem\">";
                echo "<p>" . substr($descricao, 0, 200) . "...</p>";
                echo "</a>";
                echo '</div>';
            }
            ?>
        </section>

        <hr>
        <h2>Anúncios mais antigos</h2>
        <section class="card-sec">
            <?php
            // Faz a consulta no banco de dados para obter os 3 anúncios mais antigos
            $sql = "SELECT * FROM Anuncio ORDER BY DataHora ASC LIMIT 3";
            $stmt = $pdo->prepare($sql);
            $stmt->execute();
            $resultado = $stmt->fetchAll(PDO::FETCH_ASSOC);

            foreach ($resultado as $row) {
                $codigoAnuncio = $row['Codigo'];
                $titulo = $row['Titulo'];
                $descricao = $row['Descricao'];
                $preco = $row['Preco'];
                $preco = number_format($preco, 2, ',', '.');

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
                echo "<img src=\"img/server/$imagem\" alt=\"Imagem\">";
                echo "<p>" . substr($descricao, 0, 200) . "...</p>";
                echo "</a>";
                echo '</div>';
            }
            ?>
        </section>

    </main>
    <footer>
        <p>O CrowSpot é um portal de anúncios online que permite que qualquer pessoa possa comprar, vender
            ou trocar produtos de forma fácil e segura. <br> Ao usar o CrowSpot, você concorda com nossos <a
                href="sobre.html">Termos e Condições</a> e
            com a nossa <a href="sobre.html">Política de Privacidade</a>. <br>
        </p>
        <address>CrowSpot S.A. - Rua Corvo, 123, Bairro Crowtown, CorvoCity, CrowNest - Fale conosco:
            contato@crowspot.com.br
        </address>
        <p id="dir">© CrowSpot. Todos os direitos reservados.</p>
    </footer>

</body>

<?php $pdo = null; ?>

</html>
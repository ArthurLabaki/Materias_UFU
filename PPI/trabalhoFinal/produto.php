<?php

require "php/conexaoMysql.php";

$pdo = mysqlConnect();

// Verifica se o parâmetro "codigo" foi passado na URL
if (isset($_GET['codigo'])) {
    $codigoAnuncio = $_GET['codigo'];
} else {
    // Redireciona para a página anterior caso não tenha sido passado o código do anúncio
    header("Location: index.php");
    exit();
}

// Realiza a busca no banco de dados com base no Codigo do Anuncio
$sql = "SELECT Anuncio.Codigo, Anuncio.Titulo, Anuncio.Descricao, Anuncio.Preco, Anuncio.Bairro,
               Anuncio.Cidade, Anuncio.Estado, Anuncio.CodCategoria,
               (SELECT Foto.NomeArqFoto FROM Foto WHERE Foto.CodAnuncio = Anuncio.Codigo LIMIT 1) AS NomeArqFoto
        FROM Anuncio
        WHERE Anuncio.Codigo = :codigoAnuncio";

$stmt = $pdo->prepare($sql);
$stmt->bindParam(':codigoAnuncio', $codigoAnuncio);
$stmt->execute();
$resultado = $stmt->fetch(PDO::FETCH_ASSOC);

// Verifica se o anúncio existe
if (!$resultado) {
    // Redireciona para a página anterior caso o anúncio não seja encontrado
    header("Location: index.php");
    exit();
}

$titulo = $resultado['Titulo'];
$descricao = $resultado['Descricao'];
$preco = $resultado['Preco'];
$bairro = $resultado['Bairro'];
$cidade = $resultado['Cidade'];
$estado = $resultado['Estado'];
$codigoCategoria = $resultado['CodCategoria'];
$imagem = $resultado['NomeArqFoto'];

$sqlCategoria = "SELECT Nome FROM Categoria WHERE Codigo = :codigoCategoria";
$stmtCategoria = $pdo->prepare($sqlCategoria);
$stmtCategoria->bindParam(':codigoCategoria', $codigoCategoria);
$stmtCategoria->execute();
$categoria = $stmtCategoria->fetchColumn();

$sqlImagens = "SELECT NomeArqFoto FROM Foto WHERE CodAnuncio = :codigoAnuncio";
$stmtImagens = $pdo->prepare($sqlImagens);
$stmtImagens->bindParam(':codigoAnuncio', $codigoAnuncio);
$stmtImagens->execute();
$imagens = $stmtImagens->fetchAll(PDO::FETCH_COLUMN);
?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="description"
        content="Transforme seus negócios em uma experiência incrivelmente fácil e rápida com o CrowSpot, o portal de anúncios definitivo para compras e vendas na web!">
    <link rel="stylesheet" href="css/style.css">
    <script src="js/script.js"></script>
    <title>CrowSpot - Produto</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const imagens = document.querySelectorAll('.imagens img');
        let indice = 0;

        document.querySelector('#proximo').addEventListener('click', () => {
            imagens[indice].classList.remove('active');
            indice = (indice + 1) % imagens.length;
            imagens[indice].classList.add('active');
        });
        document.querySelector('#anterior').addEventListener('click', () => {
            imagens[indice].classList.remove('active');
            indice = (indice - 1 + imagens.length) % imagens.length;
            imagens[indice].classList.add('active');
        });
    });

</script>
<style>
    main .fullCard {
        border-width: 4px;
        border-style: dashed;

        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;

        padding: 20px;
        max-width: fit-content;
        width: 100%;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    main .fullCard p {
        line-height: 1.5;
        margin: 0;
    }

    main .fullCard .esq {
        flex-basis: 55%;
        order: 1;
        display: flex;
        justify-content: space-between;
        align-items: center;
        text-align: center;

    }

    main .fullCard .esq button {
        margin-right: 15px;
        margin-left: 15px;
        background: none;
        border: none;
        cursor: pointer;
    }

    main .fullCard .esq .imagens img {
        max-width: 500px;
        min-width: 250px;
        width: 90%;
        height: auto;
        display: none;
    }

    main .fullCard .esq .imagens img.active {
        display: inline-block;
        border: 2px solid black;
        border-radius: 25px;
    }

    main .fullCard .dir {
        flex-basis: 40%;
        order: 2;
        text-align: right;
        padding-right: 10px;
    }

    main .fullCard .dir h2 {
        font-size: 30px;
    }

    main .fullCard .dir h3 {
        font-size: 20px;
    }

    main .fullCard .dir button {
        border-radius: 25px;
        border: 3px solid #000000;
        background-color: rgb(230, 230, 230);
        font-size: 20px;
        text-align: center;
        cursor: pointer;
        text-decoration: none;
        color: black;
        margin-top: 20px;
        padding: 5px 10px;
    }

    main .fullCard .dir button:hover {
        background-color: rgb(200, 200, 200);
    }

    main .fullCard .end {
        flex-basis: 100%;
        order: 3;

        margin-top: 30px;
        padding: 20px 20px;
        border: 2px solid black;
        border-radius: 35px;

    }

    main .fullCard .end h3 {
        text-align: center;
        margin-top: 0;
        font-size: 20px;
    }

    main .fullCard .end p {
        text-align: justify;
    }

    @media (max-width: 1230px) {
        main .fullCard {
            flex-direction: column;
        }

        main .fullCard .esq {
            flex-basis: auto;
            order: 1;

            display: flex;
            flex-direction: column;
            align-items: center;
        }

        main .fullCard .dir {
            flex-basis: auto;
            order: 2;
            text-align: center;
        }

        main .fullCard .end {
            flex-basis: 100%;
            order: 3;
        }
    }
</style>

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
        <div class="fullCard">
            <div class="dir">
                <h2>
                    <?php echo $titulo; ?>
                </h2>
                <h3>Preço anunciado: R$
                    <?php echo number_format($preco, 2, ',', '.') ?>
                </h3>
                <h3>Categoria:
                    <?php echo $categoria; ?>
                </h3>
                <h3>Localização do anúncio:<br>
                    <?php echo "$bairro, $cidade, $estado"; ?>
                </h3>
                <button type="button" onclick="window.location.href = 'login.html';">Contatar Anunciante!</button>
            </div>
            <div class="esq">
                <button id="anterior">
                    <img src="img/back.png" class="imgBtn" alt="Expandir">
                </button>
                <div class="imagens">
                    <?php foreach ($imagens as $index => $imagem) { ?>
                        <img <?php echo ($index === 0) ? 'class="active"' : ''; ?> src="img/server/<?php echo $imagem; ?>"
                            alt="Img<?php echo $index; ?>">
                    <?php } ?>
                </div>
                <button id="proximo">
                    <img src="img/forward.png" class="imgBtn" alt="Expandir">
                </button>
            </div>
            <div class="end">
                <h3>Descrição do Produto:</h3>
                <p>
                    <?php echo $descricao; ?>
                </p>
            </div>
        </div>
    </main>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const imagens = document.querySelectorAll('.imagens img');
            let indice = 0;

            document.querySelector('#proximo').addEventListener('click', () => {
                imagens[indice].classList.remove('active');
                indice = (indice + 1) % imagens.length;
                imagens[indice].classList.add('active');
            });
            document.querySelector('#anterior').addEventListener('click', () => {
                imagens[indice].classList.remove('active');
                indice = (indice - 1 + imagens.length) % imagens.length;
                imagens[indice].classList.add('active');
            });
        });

    </script>
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
<?php

require "conexaoMysql.php";
require "sessionVerification.php";

session_start();
exitWhenNotLoggedIn();

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="description"
        content="Transforme seus negócios em uma experiência incrivelmente fácil e rápida com o CrowSpot, o portal de anúncios definitivo para compras e vendas na web!">
    <link rel="stylesheet" href="../css/style.css">
    <script src="../js/script.js"></script>
    <title> CrowSpot - Criar Anuncio </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        main {
            background-color: darkgray;

            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .anuncio-box {
            background-color: white;
            border: 3px dashed black;

            padding: 25px;
            width: 800px;
            height: auto;
            margin-top: 4%;
            margin-bottom: 4%;
        }

        main .anuncio-box h1 {
            margin-top: 0;
            margin-bottom: 25px;
        }

        main .anuncio-box .formu {
            display: flex;
            flex-wrap: wrap;
        }

        main .anuncio-box .textbox {
            display: flex;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
        }

        main .anuncio-box .textbox input {
            background-color: white;
            border: 3px solid black;
            border-radius: 25px;

            width: 95%;
            max-width: 550px;
            height: 40px;
            margin-left: 3%;
            padding-left: 20px;

        }

        main .anuncio-box .textbox select {
            background-color: white;
            border: 3px solid black;
            border-radius: 15px;

            width: 95%;
            max-width: 300px;
            height: 40px;
            margin-left: 3%;
            padding-left: 20px;
        }

        main .anuncio-box .textbox textarea {
            background-color: white;
            border: 3px solid black;
            border-radius: 5px;

            width: 95%;
            max-width: 550px;
            height: 80px;
            margin-left: 3%;
            padding-left: 20px;
            padding-top: 10px;
        }


        main .anuncio-box .textbox label {
            font-size: large;
            margin-bottom: 5px;
        }

        main .anuncio-box .textbox #imagens {
            background-color: white;
            border: 0;
            text-align: center;

            width: 95%;
            max-width: 350px;
            height: 40px;
            margin-left: 3%;
            padding-left: 20px;
            margin-top: 10px;
        }

        main .anuncio-box #log .btn {
            border-radius: 25px;
            border: 3px solid #000000;
            background-color: rgb(230, 230, 230);
            font-size: 20px;
            text-align: center;
            cursor: pointer;
            text-decoration: none;
            color: black;

            padding: 15px 20px;
            margin-top: 20px;
        }

        main .anuncio-box #log .btn:hover {
            background-color: rgb(200, 200, 200);
        }
    </style>
</head>

<body>
    <header>
        <a href="index.php">
            <img src="../img/Logo_CrowSpot.png" alt="CrowSpot - portal de anúncios">
        </a>
        <a href="home.php" class="button">Home</a>
    </header>
    <nav>
        <form id="searchForm">
            <div id="divBusca">
                <input type="text" id="inpBusca" placeholder="Buscar...">
                <button id="btnExp" type="button" title="Opções avançadas">
                    <img src="../img/expand.png" class="imgBtn" alt="Expandir">
                </button>
                <button id="btnBusca" type="submit" title="Buscar">
                    <img src="../img/lupa.png" class="imgBtn" alt="Buscar">
                </button>
            </div>
        </form>
        <script>
            document.getElementById('searchForm').addEventListener('submit', function (event) {
                event.preventDefault(); // Impede o envio padrão do formulário
                var mainElement = document.querySelector('main');
                mainElement.innerHTML = '';
                mainElement.style.backgroundColor = "white";

                // Remover os atributos display, align-items, justify-content e text-align
                mainElement.style.display = "";
                mainElement.style.alignItems = "";
                mainElement.style.justifyContent = "";
                mainElement.style.textAlign = "";

                var query = document.getElementById('inpBusca').value;
                var searchField = getSearchField();
                var minPrice = document.getElementById('inpMin').value;
                var maxPrice = document.getElementById('inpMax').value;
                var categories = getSelectedCategories();
                var currentPage = 1; // Página inicial

                function loadResults(page) {
                    fetch('buscaProduto.php', {
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
                                    imgElement.src = '../img/server/' + item.imagem;
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
            fetch("categorias.php")
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
        <div class="anuncio-box">
            <h1>Criar Novo Anúncio</h1>
            <div class="formul">
                <form name="formAnun">
                    <div class="textbox">
                        <label for="titulo">Título: </label>
                        <input type="text" placeholder=" Digite o título" name="titulo" id="titulo" required
                            maxlength="50">
                    </div>

                    <div class="textbox">
                        <label for="val">Valor: </label>
                        <input type="number" placeholder=" Digite o valor" name="val" id="val" required max="9999999"
                            min="0">
                    </div>

                    <div class="textbox">
                        <label for="cep">CEP: </label>
                        <input type="text" placeholder=" Digite o CEP (ex: 12345-678)" name="cep" id="cep" required
                            pattern="[0-9]{5}-[0-9]{3}">
                    </div>

                    <div class="textbox">
                        <label for="bar">Bairro: </label>
                        <input type="text" placeholder=" Digite o bairro" name="bar" id="bar" required>
                    </div>

                    <div class="textbox">
                        <label for="city">Cidade: </label>
                        <input type="text" placeholder=" Digite a cidade" name="city" id="city" required>
                    </div>

                    <div class="textbox">
                        <label for="est">Estado: </label>
                        <input type="text" placeholder=" Digite o estado" name="est" id="est" required>
                    </div>

                    <div class="textbox">
                        <label for="desc">Descrição: </label>
                        <textarea placeholder="Digite a descrição do produto" name="desc" id="desc" required></textarea>
                    </div>

                    <div class="textbox">
                        <label for="cat">Categoria: </label>
                        <select name="cat" id="cat" required>
                            <option value="" selected disabled hidden>Selecione alguma categoria</option>
                            <option value="inv">Invalido</option>
                        </select>
                    </div>

                    <div class="textbox">
                        <label for="imagens">Imagens:</label>
                        <input type="file" name="imagens[]" id="imagens" accept="image/*" multiple required>
                    </div>

                    <div id="log">
                        <input type="submit" class="btn" value="Criar">
                    </div>
                </form>
            </div>
        </div>
        <script>

            async function buscaEndereco(cep) {
                if (cep.length != 9) return;

                try {
                    let response = await fetch("busca-end.php?cep=" + cep);
                    if (!response.ok) throw new Error(response.statusText);
                    var endereco = await response.json();
                    console.log(endereco)
                }
                catch (e) {
                    console.error(e);
                    return;
                }

                let form = document.forms.formAnun;
                form.bar.value = endereco.bairro;
                form.city.value = endereco.cidade;
                form.est.value = endereco.estado;
            }

            window.addEventListener('load', function () {
                const inputCep = document.querySelector("#cep");
                inputCep.addEventListener('keyup', () => buscaEndereco(inputCep.value));
            });

            const selectCat = document.getElementById("cat");

            fetch("categorias.php")
                .then(response => response.json())
                .then(data => {
                    // Limpar as opções existentes
                    selectCat.innerHTML = "";
                    console.log(data)
                    // Adicionar a opção padrão
                    const defaultOption = document.createElement("option");
                    defaultOption.value = "";
                    defaultOption.textContent = "Selecione alguma categoria";
                    defaultOption.disabled = true;
                    defaultOption.hidden = true;
                    defaultOption.selected = true;
                    selectCat.appendChild(defaultOption);

                    // Adicionar as opções do JSON recebido
                    data.forEach(categoria => {
                        const option = document.createElement("option");
                        option.value = categoria.Nome;
                        option.textContent = categoria.Nome;
                        selectCat.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error("Erro ao carregar as categorias:", error);
                });
            async function sendForm(form) {
                try {
                    // Envia a requisição assíncrona com o método POST
                    const response = await fetch("sAnuncio.php", {
                        method: 'POST',
                        body: new FormData(form)
                    });

                    // Verifica se a resposta da requisição está OK
                    if (response.ok) {
                        const result = await response.json();
                        if (result.success) {
                            // Cadastro realizado com sucesso
                            window.location = result.detail;
                        } else {
                            // Exibe mensagem de erro
                            console.log(result.detail);
                        }
                    } else {
                        // Exibe mensagem de erro caso a requisição não tenha sido bem-sucedida
                        console.error('Erro na requisição:', response.status, response.statusText);
                    }
                } catch (error) {
                    // Exibe mensagem de erro em caso de exceção
                    console.error('Erro na requisição:', error);
                }
            }

            window.addEventListener('load', function () {
                const form = document.forms.formAnun;
                form.onsubmit = function (e) {
                    sendForm(form);
                    e.preventDefault();
                };
            });


        </script>
    </main>

    <footer>
        <p>O CrowSpot é um portal de anúncios online que permite que qualquer pessoa possa comprar, vender
            ou trocar produtos de forma fácil e segura. <br> Ao usar o CrowSpot, você concorda com nossos <a
                href="sobre.php">Termos e Condições</a> e
            com a nossa <a href="sobre.php">Política de Privacidade</a>. <br>
        </p>
        <address>CrowSpot S.A. - Rua Corvo, 123, Bairro Crowtown, CorvoCity, CrowNest - Fale conosco:
            contato@crowspot.com.br
        </address>
        <p id="dir">© CrowSpot. Todos os direitos reservados.</p>
    </footer>
</body>

</html>
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
    <title> CrowSpot - Sobre </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        hr {
            color: black;
            border-width: 2px;
            border-style: dashed;
            margin-top: 15px;
            margin-bottom: 25px;
            width: 100%;
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
        <h1>CrowSpot, anunciar seus produtos nunca foi tão fácil!</h1>
        <p>A CrowSpot nasceu em 2024 com o objetivo de criar uma plataforma de anúncios online que fosse
            simples e eficiente para conectar compradores e vendedores de produtos de todo o país. Desde então, temos
            trabalhado duro para oferecer a melhor experiência de anúncios para nossos usuários, com tecnologia de
            ponta, segurança e confiança. </p>
        <hr>

        <h2>Nossa Missão</h2>
        <p>Nossa missão é tornar mais fácil e acessível a compra e venda de produtos online. Queremos ser a primeira
            escolha de quem procura uma plataforma de anúncios confiável e segura para fazer negócios com agilidade
            e
            praticidade.</p>
        <hr>

        <h2>Nossos valores</h2>
        <p>A CrowSpot é uma empresa que preza por valores fundamentais em seu dia a dia, buscando oferecer aos seus
            usuários uma plataforma de anúncios online segura, eficiente e acessível. Nós acreditamos que a excelência é
            um dos pilares de nosso sucesso e, por isso, estamos sempre em busca de oferecer o melhor atendimento e
            tecnologia disponível no mercado.</p>
        <p>A transparência é outro valor importante em nosso trabalho. Sabemos que a confiança é essencial para qualquer
            negociação e, por isso, buscamos manter uma comunicação clara e honesta com nossos clientes, garantindo que
            todas as transações ocorram de forma transparente e confiável.</p>
        <p>Inovação é outro pilar da CrowSpot. Acreditamos que a busca constante por soluções e tecnologias inovadoras é
            essencial para oferecer aos nossos usuários uma experiência única e eficiente. Por isso, estamos sempre em
            constante evolução, trazendo novas funcionalidades e melhorias para a plataforma.</p>
        <p>A empatia é um valor que nos move. Entendemos que cada usuário é único e tem necessidades diferentes, por
            isso buscamos ouvir e entender as demandas de cada um, oferecendo um atendimento personalizado e cuidadoso
            em todas as etapas da negociação.</p>
        <p>Por fim, a segurança é um valor essencial para a CrowSpot. Investimos em tecnologia avançada e processos
            rigorosos de segurança para garantir que nossos usuários possam realizar suas transações com tranquilidade e
            confiança, sabendo que seus dados e informações estão protegidos em nossa plataforma.</p>
        <hr>

        <h2>Termos e Condições</h2>
        <p>Ao utilizar os serviços da plataforma CrowSpot, você concorda com os termos e condições descritos abaixo:</p>
        <h3>Cadastro</h3>
        <p>Para utilizar os serviços da CrowSpot, é necessário realizar um cadastro informando seus dados pessoais. Ao
            realizar o cadastro, você concorda em fornecer informações verdadeiras, completas e precisas sobre si mesmo,
            mantendo seus dados atualizados e corretos.</p>
        <h3>Anúncios</h3>
        <p>Ao criar um anúncio na plataforma CrowSpot, você se responsabiliza por fornecer informações verdadeiras e
            completas sobre o produto anunciado. Além disso, você concorda em não anunciar produtos ilegais,
            falsificados, de procedência duvidosa ou que possam causar danos aos usuários ou à plataforma.</p>
        <h3>Compra e venda</h3>
        <p>A CrowSpot é uma plataforma de anúncios online, portanto, não nos responsabilizamos por qualquer negociação
            realizada entre comprador e vendedor. O papel da CrowSpot é conectar compradores e vendedores, oferecendo
            uma plataforma segura e eficiente para realização de negociações.</p>
        <h3>Segurança</h3>
        <p>A CrowSpot investe em tecnologia avançada e processos rigorosos de segurança para garantir que seus usuários
            possam realizar suas transações com tranquilidade e confiança, sabendo que seus dados e informações estão
            protegidos em nossa plataforma. No entanto, não nos responsabilizamos por quaisquer danos ou prejuízos
            causados por terceiros ou por ações de usuários mal-intencionados.</p>
        <h3>Alterações nos termos e condições</h3>
        <p>A CrowSpot se reserva o direito de alterar estes termos e condições a qualquer momento, sem aviso prévio. É
            de responsabilidade dos usuários manter-se informados sobre as atualizações realizadas.</p>
        <hr>

        <h2>Política de Privacidade</h2>
        <p>A privacidade dos usuários da CrowSpot é de extrema importância para nós. Por isso, adotamos medidas de
            segurança e privacidade para garantir a proteção das informações pessoais fornecidas pelos usuários. Ao
            utilizar a plataforma CrowSpot, você concorda com os termos descritos abaixo:</p>
        <h3>Coleta de informações</h3>
        <p>Ao se cadastrar na plataforma CrowSpot, coletamos as informações pessoais necessárias para a utilização dos
            serviços oferecidos. Essas informações incluem nome, endereço de e-mail, telefone e outros.
        </p>
        <h3>Uso das informações</h3>
        <p>As informações pessoais coletadas pela CrowSpot são utilizadas exclusivamente para a prestação dos serviços
            oferecidos pela plataforma, bem como para a melhoria contínua da experiência dos usuários. Não divulgamos
            informações pessoais dos usuários para terceiros, exceto nos casos previstos em lei ou por solicitação
            judicial.</p>
        <h3>Cookies</h3>
        <p>A CrowSpot utiliza cookies para melhorar a experiência dos usuários na plataforma. Os cookies são arquivos de
            texto armazenados no computador do usuário que permitem a identificação do usuário na plataforma e a
            personalização da experiência de navegação.</p>
        <h3>Links externos</h3>
        <p>A plataforma CrowSpot pode conter links para sites de terceiros. Não nos responsabilizamos pelas práticas de
            privacidade desses sites, por isso recomendamos que os usuários leiam as políticas de privacidade de cada
            site acessado.</p>
        <h3>Alterações na política de privacidade</h3>
        <p>A CrowSpot se reserva o direito de alterar estas politicas de privacidade a qualquer momento, sem aviso
            prévio. É
            de responsabilidade dos usuários manter-se informados sobre as atualizações realizadas.</p>
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
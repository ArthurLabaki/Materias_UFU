<!doctype html>
<html lang="pt-br">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>File Jolt</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <link href="../_css/estilo.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400&display=swap" rel="stylesheet">
    <style>
        .all {
            margin-left: 10%;
            margin-top: 2%;
            margin-bottom: 4%;
        }

        .tit {
            text-align: center;
            margin-left: -1%;
        }

        h5 {
            margin-top: 5%;
            margin-left: 14%;
            color: azure;
        }

        a {
            text-decoration: none;
        }

        h2 {
            text-align: left;
            margin-top: 2%;
            margin-left: 3.5%;
            margin-bottom: 6%;
        }

        h4 {
            margin-top: 2%;
            margin-left: 8%;
            margin-bottom: 6%;
        }


        h6 {
            margin-top: 8%;
            margin-left: 8%;
        }

        .cfile {
            text-align: right;
            font-size: larger;
            margin-top: 3%;
            margin-right: 2%;
        }

        .but {
            color: black;
            padding: 1.5%;
            margin-top: 1%;
            margin-bottom: 2.5%;
            margin-left: 7%;
            width: 70%;
            font-size: large;
        }

        .exemp {
            margin-right: 10%;
            height: 200px;
            width: 65%;
            background-image: linear-gradient(to bottom, rgb(102, 255, 0), rgb(0, 183, 255));
            margin-top: 1%;
        }

        .quadros {
            margin: auto;
            padding-bottom: 1%;
        }

        .exemplo {
            height: 165px;
            width: 220px;
            background-color: blue;
            padding: 2%;
        }

        .file {
            text-decoration: none;
            color: azure;
        }

        .file:hover {
            color: azure;
        }

        .alt {
            text-align: center;
            margin-top: 10%;
            padding-right: 10%;
        }
    </style>

</head>

<body>
    <nav class="navbar navbar-expanded">
        <div class="container-fluid">

            <a class="navbar-brand p-20" href="../" alt="Logo File Jolt">
                <img src="../_img/logo1.png" />
            </a>

            <form class="d-flex">
                <div class="form-group mx-2">
                    <input class="form-control" type="text" placeholder="Pesquisa">
                </div>
                <a href="../busca">
                    <button type="button" class="btn btn-light m-auto" id="pesqisa-btn"> Pesquisar </button>
                </a>
            </form>

            <a href="../login">
                <button type="button" class="btn btn-light" id="login-btn"> Login </button>
            </a>
        </div>
    </nav>
    <!-- Perfil do usuário-->
    <main>
        <div class="container pb-5">

            <div class="row">
                <div class="files col-sm-11 m-auto p-4 pb-5 border border-3 border-dark" id="files">
                    <div class="row">
                        <div class="col-6">
                            <h2>Seus files:</h2>
                        </div>
                        <div class="col-6">
                            <a class="file" href="../criararquivo/">
                                <h2 class="cfile">Criar um novo file</h2>
                            </a>
                        </div>
                    </div>
                    <div class="row">
                        <div class="quadros col-sm-3 border border-2 border-dark">
                            <h5>Título do File</h5>
                            <div class="exemplo m-auto border border-1 border-dark"></div>
                            <div class="col">
                                <h6>Votos: Número</h6>
                            </div>
                            <div class="col">
                                <h6>Downloads: Número</h6>
                            </div>
                            <div class="col">
                                <h6>Comentários: Número</h6>
                            </div>
                            <div class="col">
                                <a class="file" href="../modificararquivo/">
                                    <h6 class="alt">Alterar File</h6>
                                </a>
                            </div>
                        </div>

                        <div class="quadros col-sm-3 border border-2 border-dark">
                            <a class="file" href="../file">
                                <h5>Título do File</h5>
                                <div class="exemplo m-auto border border-1 border-dark"></div>
                                <div class="col">
                                    <h6>Votos: Número</h6>
                                </div>
                                <div class="col">
                                    <h6>Downloads: Número</h6>
                                </div>
                                <div class="col">
                                    <h6>Comentários: Número</h6>
                                </div>
                            </a>
                            <div class="col">
                                <a class="file" href="../modificararquivo/">
                                    <h6 class="alt">Alterar File</h6>
                                </a>
                            </div>
                        </div>

                        <div class="quadros col-sm-3 border border-2 border-dark">
                            <h5>Título do File</h5>
                            <div class="exemplo m-auto border border-1 border-dark"></div>
                            <div class="col">
                                <h6>Votos: Número</h6>
                            </div>
                            <div class="col">
                                <h6>Downloads: Número</h6>
                            </div>
                            <div class="col">
                                <h6>Comentários: Número</h6>
                            </div>
                            <div class="col">
                                <a class="file" href="../modificararquivo/">
                                    <h6 class="alt">Alterar File</h6>
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <div class="row mt-5">
                <div class="files col-sm-11 m-auto p-4 pb-5 border border-3 border-dark" id="files">
                    <h2 class="tit">Configurações</h2>
                    <div class="all row">
                        <div class="col-sm-4">
                            <div class="exemp border border-4 border-dark"></div>
                            <a href="#">
                                <h5>Trocar avatar</h5>
                            </a>
                        </div>
                        <div class="col-sm-8">
                            <div class="row">
                                <a href="#">
                                    <button class="but btn btn-outline-secondary btn-light" type="button">Alterar
                                        email</button>
                                </a>

                                <a href="#">
                                    <button class="but btn btn-outline-secondary btn-light" type="button">Alterar nome
                                        de
                                        usuário</button>
                                </a>
                                <a href="#">
                                    <button class="but btn btn-outline-secondary btn-light" type="button">Alterar
                                        senha</button>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <div class="footer">
            <p id="foot">© 2022 Todos os direitos reservados <br> Desenvolvido por Alexandre Petusk, Arthur Labaki,
                Klesley Oliveira, Túlio Roquete e Wellington Cesar
            </p>
        </div>
    </footer>
    <!-- Fim -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
        crossorigin="anonymous"></script>
</body>

</html>
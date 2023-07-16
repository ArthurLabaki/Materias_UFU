// Função da janela modal vai ser acionada ao carregar todos os elementos do DOM da página
window.onload = function () {

    // Cria as variáveis 'modal' e 'btnClose' que são atreladas as classes da janela modal e o botão de fechar respectivamente
    const modal = document.querySelector(".modal");
    const btnClose = modal.querySelector(".btnClose");

    // Ao clicar no botão de fechar janela modal, vai executar a função
    btnClose.addEventListener("click", function () {
        // modifica o display do modal para não aparecer (invisivel)
        modal.style.display = 'none';
    });

    // Cria a variavel 'btnOpen' que é atrelada ao id do botão de abrir janela modal
    const btnOpen = document.getElementById("btnExp");

    // Ao clicar no botão de abrir janela modal, vai executar a função
    btnOpen.addEventListener("click", function () {
        // modifica o display do modal para aparecer (visivel)
        modal.style.display = 'block';
    })
    // Função para mostrar o botão de opções avancadas
    function showBtn() {
        document.getElementById("btnExp").style.visibility = "visible";
    }
    // Função para esconder o botão de opções avancadas, com um delay para permitir o click
    function hideBtn() {
        setTimeout(function () {
            document.getElementById("btnExp").style.visibility = "hidden";
        }, 200);
    }
    // Obter o elemento do input
    var input = document.getElementById("inpBusca");

    // Adicionar o evento "onfocus"
    input.addEventListener("focus", showBtn);

    // Adicionar o evento "onblur"
    input.addEventListener("blur", hideBtn);
}


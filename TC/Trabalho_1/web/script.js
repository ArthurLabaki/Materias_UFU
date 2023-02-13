const ELEMS_IN_CONTAINER = 10;

let transitionRow = 0;
let renderDone = false;
let jsonResult = null;

// global elements
let container = document.getElementById("squares_container");
let seta = document.getElementById("seta");
let nextButton = document.getElementById("next_button");
let previewButton = document.getElementById("preview_button");
let automaticButton = document.getElementById("automatic_button");
let tableTransition = document.getElementById("table_transition");
let mtActualState = document.getElementById("mt_actual_state");
let mtState = document.getElementById("mt_state");

// get MT json
async function getMTJson(){

    try{
        jsonResult = await eel.getPythonMTJson()();

        renderDone = true;
        renderBlocks();
        renderSeta();
        renderTransitionTable();
        renderProcessTable();
    }
    catch(e){
        console.log(e);
    }
}
getMTJson();

// render blocks dynamic
function renderBlocks(){

    if(renderDone && jsonResult != null){

        let innerHtml = '';
        let first = true;

        // updates cadeia
        let cadeiaTmp = jsonResult["processamento"][transitionRow]["cadeia"];

        let cadeia = [];
        for(let i = 0; i < ELEMS_IN_CONTAINER || i < cadeiaTmp.length; i++){
            cadeia.push( i < cadeiaTmp.length ? cadeiaTmp[i] : ' ' );
        }

        cadeia.forEach(simbolo => {
            if(first){
                innerHtml += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
                first = false;
            }
            else{
                innerHtml += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
            }
        });
        innerHtml += '';
        container.style.width = 34*ELEMS_IN_CONTAINER + 6 + 'px';
        container.innerHTML = innerHtml;
    }
}

// render arrow
function renderSeta(){

    if(renderDone && jsonResult != null){

        let setaPosition = jsonResult["processamento"][transitionRow]["posicao_fita"];

        let linePosition = Math.floor(setaPosition/ELEMS_IN_CONTAINER);
        let rowPosition = setaPosition%ELEMS_IN_CONTAINER;
        seta.style.top = "calc(100% + " + ( 69*linePosition + 5 ) + "px)";
        seta.style.left = 3.5 + 34*rowPosition + "px";
    }
}

// next and preview Button
nextButton.addEventListener('click', nextTransition);
previewButton.addEventListener('click', previewTransition);
automaticButton.addEventListener('click', automaticTransition);
previewButton.disabled = true;

function nextTransition(){

    if(renderDone && jsonResult != null){

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];

        if(transition == "inicial"){
            previewButton.disabled = false;
        }

        if(transition != "aceita" && transition != "rejeitada"){
            transitionRow += 1;
            renderBlocks();
            renderSeta();
            renderTransitionTable();
            renderProcessTable();

            transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
            console.log(typeof transition)
            if(transition == "aceita" || transition == "rejeitada"){
                nextButton.disabled = true;
            }
        }
    }
}

function previewTransition(){

    if(renderDone && jsonResult != null){

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];

        if(transition == "aceita" || transition == "rejeitada"){
            nextButton.disabled = false;
        }

        if(transition != "inicial"){
            transitionRow -= 1;
            renderBlocks();
            renderSeta();
            renderTransitionTable();
            renderProcessTable();

            transition = jsonResult["processamento"][transitionRow]["transicao_usada"];

            if(transition == "inicial"){
                previewButton.disabled = true;
            }
        }
    }
}

function renderTransitionTable(){
   
    if(renderDone && jsonResult != null){
        let innerHTML = '';

        let transitionN = jsonResult["processamento"][transitionRow]["transicao_usada"];
        let jsonTransitions = jsonResult["transicoes"];

        console.log(jsonTransitions);

        for(let i = 0; i < jsonTransitions.length; i++ ) {
    
            if(i == transitionN) {
                let value = '<tr><td style="background-color: hsl(240, 100%, 90%);">' + jsonTransitions[i] + '</td></tr>';
                innerHTML += value;
            }
            else {
                let value = '<tr><td>' + jsonTransitions[i] + '</td></tr>';
                innerHTML += value;
            }

        }
        tableTransition.innerHTML = innerHTML;
    }
}

function renderProcessTable(){

    if(renderDone && jsonResult != null){

        let actualState = jsonResult["processamento"][transitionRow]["estado_atual"];
        let usedTransiction = jsonResult["processamento"][transitionRow]["transicao_usada"];

        console.log(actualState);
        mtActualState.innerHTML = actualState;
        mtState.innerHTML = usedTransiction == 'inicial' ? 'iniciando' : ( usedTransiction == 'aceita' || usedTransiction == 'rejeitada' ? usedTransiction : 'processando' );
    }
}

async function automaticTransition(){
    
    if(renderDone && jsonResult != null){

        previewButton.style.display = 'none';
        nextButton.style.display = 'none';

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
        while(transition != "aceita" && transition != "rejeitada"){
            nextTransition();
            await new Promise(r => setTimeout(r, 500));
            transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
        }

        previewButton.style.display = 'block';
        nextButton.style.display = 'block';
    }

}

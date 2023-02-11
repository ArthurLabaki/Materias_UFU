const ELEMS_IN_CONTAINER = 30;

let transitionRow = 0;
let renderDone = false;
let jsonResult = null;

// global elements
let squaresContainer1 = document.getElementById("squares_container1");
let squaresContainer2 = document.getElementById("squares_container2");
let seta1 = document.getElementById("seta1");
let seta2 = document.getElementById("seta2");
let cadeiaInput1 = document.getElementById("cadeia_input1");
let cadeiaInput2 = document.getElementById("cadeia_input2");
let doProcessButton = document.getElementById("do_process_button");
let nextButton = document.getElementById("next_button");
let previewButton = document.getElementById("preview_button");
let automaticButton = document.getElementById("automatic_button");
let tableTransition = document.getElementById("table_transition");
let mtActualState = document.getElementById("mt_actual_state");
let mtState = document.getElementById("mt_state");
let mtTimestamp = document.getElementById("mt_timestamp");
let mtIterations = document.getElementById("mt_iterations");
let tableHolder = document.getElementById("table_holder");
let tableProcessHolder = document.getElementById("table_process_holder");

// disable or not render elements on start
seta1.style.display = 'none';
seta2.style.display = 'none';
tableHolder.style.display = 'none';
tableProcessHolder.style.display = 'none';
nextButton.style.display = 'none';
previewButton.style.display = 'none';
automaticButton.style.display = 'none';
previewButton.disabled = true;

// event listener
doProcessButton.addEventListener('click', getMTJson);
nextButton.addEventListener('click', nextTransition);
previewButton.addEventListener('click', previewTransition);
automaticButton.addEventListener('click', automaticTransition);

// get MT result json
async function getMTJson(){

    transitionRow = 0;
    renderDone = false;
    jsonResult = null;

    seta1.style.display = 'block';
    seta2.style.display = 'block';
    tableHolder.style.display = 'block';
    tableProcessHolder.style.display = 'block';
    nextButton.style.display = 'block';
    previewButton.style.display = 'block';
    automaticButton.style.display = 'block';

    try{

        let cadeia1  = cadeiaInput1.value;
        let cadeia2  = cadeiaInput2.value;

        jsonResult = await eel.getPythonMTJson(cadeia1, cadeia2)();
        renderDone = true;
        
        previewButton.disabled = true;
        if(jsonResult && 
            jsonResult["processamento"] && 
            jsonResult["processamento"].length > 0){
                nextButton.disabled = false;
        }
        else{
            nextButton.disabled = true;
        }

        renderBlocks();
        renderSeta();
        renderTransitionTable();
        renderProcessTable();
    }
    catch(e){
        console.log(e);
    }
}

// render blocks dynamic
function renderBlocks(){

    squaresContainer1.innerHTML = '';
    squaresContainer2.innerHTML = '';

    if(renderDone && jsonResult != null){

        console.log('aqui render blocks');

        let innerHtml1 = '';
        let innerHtml2 = '';
        let first = true;

        // updates fitas
        console.log(jsonResult);
        let fita1Tmp = jsonResult["processamento"][transitionRow]["fita_1"];
        let fita2Tmp = jsonResult["processamento"][transitionRow]["fita_2"];

        // fita 1
        let fita1 = [];
        for(let i = 0; i < ELEMS_IN_CONTAINER || i < fita1Tmp.length; i++){
            fita1.push( i < fita1Tmp.length ? fita1Tmp[i] : ' ' );
        }
        
        fita1.forEach(simbolo => {
            if(first){
                innerHtml1 += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
                first = false;
            }
            else{
                innerHtml1 += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
            }
        });

        squaresContainer1.style.width = 34*ELEMS_IN_CONTAINER + 6 + 'px';
        squaresContainer1.innerHTML = innerHtml1;

        // fita 2
        let fita2 = [];
        first = true;
        for(let i = 0; i < ELEMS_IN_CONTAINER || i < fita2Tmp.length; i++){
            fita2.push( i < fita2Tmp.length ? fita2Tmp[i] : ' ' );
        }

        fita2.forEach(simbolo => {
            if(first){
                innerHtml2 += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
                first = false;
            }
            else{
                innerHtml2 += `<div class="sqr_block"> <span> ${simbolo} </span> </div>`;
            }
        });

        squaresContainer2.style.width = 34*ELEMS_IN_CONTAINER + 6 + 'px';
        squaresContainer2.innerHTML = innerHtml2;
    }
}

// renders arrows
function renderSeta(){

    if(renderDone && jsonResult != null){

        let setaPosition1 = jsonResult["processamento"][transitionRow]["posicao_fita_1"];
        let setaPosition2 = jsonResult["processamento"][transitionRow]["posicao_fita_2"];

        let linePosition = Math.floor(setaPosition1/ELEMS_IN_CONTAINER);
        let rowPosition = setaPosition1%ELEMS_IN_CONTAINER;
        seta1.style.top = "calc(100% + " + ( 69*linePosition + 5 ) + "px)";
        seta1.style.left = 3.5 + 34*rowPosition + "px";

        linePosition = Math.floor(setaPosition2/ELEMS_IN_CONTAINER);
        rowPosition = setaPosition2%ELEMS_IN_CONTAINER;
        seta2.style.top = "calc(100% + " + ( 69*linePosition + 5 ) + "px)";
        seta2.style.left = 3.5 + 34*rowPosition + "px";
    }
}

// does next transiction
function nextTransition(){

    if(renderDone && jsonResult != null){

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];

        if(transition == "inicial"){
            previewButton.disabled = false;
        }

        if(transition != "ACEITA" && transition != "REJEITA"){
            transitionRow += 1;
            renderBlocks();
            renderSeta();
            renderTransitionTable();
            renderProcessTable();

            transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
            if(transition == "ACEITA" || transition == "REJEITA"){
                nextButton.disabled = true;
            }
        }
    }
}

// does preview transiction
function previewTransition(){

    if(renderDone && jsonResult != null){

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];

        if(transition == "ACEITA" || transition == "REJEITA"){
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

// renders transiction table
function renderTransitionTable(){
    
    tableTransition.innerHTML = '';

    if(renderDone && jsonResult != null){
        let innerHTML = '';

        let transitionN = jsonResult["processamento"][transitionRow]["transicao_usada"];
        let jsonTransitions = jsonResult["transicoes"];

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

// renders process table
function renderProcessTable(){

    mtState.innerHTML = '';

    if(renderDone && jsonResult != null){

        console.log(jsonResult);

        let actualState = jsonResult["processamento"][transitionRow]["estado_atual"];
        let usedTransiction = jsonResult["processamento"][transitionRow]["transicao_usada"];

        mtActualState.innerHTML = actualState;
        mtState.innerHTML = usedTransiction == 'inicial' ? 'iniciando' : ( usedTransiction == 'ACEITA' || usedTransiction == 'REJEITA' ? usedTransiction : 'processando' );
        mtTimestamp.innerHTML = jsonResult["timestamp"]
        mtIterations.innerHTML = jsonResult["iterations"]
    
    }
}

// does automatic transictions
async function automaticTransition(){
    
    if(renderDone && jsonResult != null){

        cadeiaInput1.style.display = 'none';
        cadeiaInput2.style.display = 'none';
        doProcessButton.style.display = 'none';
        previewButton.style.display = 'none';
        nextButton.style.display = 'none';
        automaticButton.disabled = true;

        let transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
        while(transition != "ACEITA" && transition != "REJEITA"){
            nextTransition();
            await new Promise(r => setTimeout(r, 250));
            transition = jsonResult["processamento"][transitionRow]["transicao_usada"];
        }

        cadeiaInput1.style.display = 'inline-block';
        cadeiaInput2.style.display = 'inline-block';
        doProcessButton.style.display = 'inline-block';
        previewButton.style.display = 'block';
        nextButton.style.display = 'block';
        automaticButton.disabled = false;
    }

}
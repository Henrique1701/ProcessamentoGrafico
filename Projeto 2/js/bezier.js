// definições
class Point{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
}

function interpolation(pointA, pointB, t){
    // Para ser interpolação verdadeira, t precisa estar entre 0 e 1. Caso não esteja deveria retornar nada/erro.
    // Porém, como essa função só é usada dentro do deCasteljau, temos controle sobre isso!
    return new Point(pointA.x * (1-t) + pointB.x * t, pointA.y * (1-t) + pointB.y * t);
}

function deCasteljau(pontos, t){
    // -1 pois o grau começa a partir do 1, mas o array começa a partir do 0.
    var grau = pontos.length - 1;
    if (grau == 1){
        return interpolation(pontos[0], pontos[1], t);
    } else {
        // nova curva
        var pontosAux = [];
        for (let i = 0; i < grau; i++){
            pontosAux.push(interpolation(pontos[i], pontos[i+1], t));
        }
        return deCasteljau(pontosAux,  t);
    }
}

// elementos da aplicação
// canvas
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

// legenda
var legendaText = document.getElementById("legenda");

// botões - curva
var newCurvaBtn = document.getElementById("newCurveBtn");
var delCurvaBtn = document.getElementById("delCurveBtn");
var previousCurveBtn = document.getElementById("previousCurveBtn");
var nextCurveBtn = document.getElementById("nextCurveBtn");

// botões - pontos
var addPontoBtn = document.getElementById("addPontoBtn");
var delPontoBtn = document.getElementById("delPontoBtn");
var movePontoBtn = document.getElementById("movePontoBtn");
var previousPontoBtn = document.getElementById("previousPontoBtn");
var nextPontoBtn = document.getElementById("nextPontoBtn");

// input e checkboxes
var numAvaliacoesInput = document.getElementById("avaliacoes");
var poligonosCheckbox = document.getElementById("poligonosCheckbox");
var pontosCheckbox = document.getElementById("pontosCheckbox");
var curvasCheckbox = document.getElementById("curvasCheckbox");

// constantes e variáveis
const POINT_RADIUS = 4; // para desenhar o ponto

// armazenamento e ponteiros
// lista de lista de pontos. Armazena todas as curvas na aplicação
var curves = []; 
curves.push([]);

var selectedCurve = -1; // aponta para a curva que está sendo operada no momento
var selectedPoint = []; // lista de ponteiros para as curvas
selectedPoint.push(0);
var numAvaliacoes = 100;

// estado do canvas: 1 - Acrescentando | 2 - Reposicionando
var stateCanvas = 0;
var clique = false;
// booleanos para os checkboxes
var showPoligonos = true;
var showPoints = true;
var showCurves = true;

// funções de desenho

// desenha o ponto
function drawPoint(point){
    ctx.beginPath();
    // desenha um arco no ponto x, y, com raio = POINT_RADIUS e circunferencia iniciando em 0 rad e indo até 2pi
    ctx.arc(point.x, point.y, POINT_RADIUS, 0, 2 * Math.PI);
    ctx.stroke();
}

// desenha a linha entre os pontos a e b
function drawLine(a, b){
    ctx.beginPath();
    ctx.lineTo(a.x, a.y);
    ctx.lineTo(b.x, b.y);
    ctx.strokeStyle = "3px";
    ctx.stroke();
}

// desenha poligonos de controle
function drawControlPolygon(pontos){
    for (let i = 0; i < pontos.length-1; i++){
        drawLine(pontos[i], pontos[i+1]);
    }
}

// desenha a curva
function drawBezierCurve(curve){
    if (curve.length > 2){
        var bezierCurves = [];
        bezierCurves.push(curve[0]);
        // a iteração é até numAvaliações - 2, pois já estão inclusos os pontos inicial e final, que são dados pelo usuário.
        for (let i = 1; i <= numAvaliacoes-2; i++){
            bezierCurves.push(deCasteljau(curve, i / numAvaliacoes));
        }
        // esse ultimo push fora do laço é para que ele não fique dando aquela sobrinha, entre a ultima avaliação e o ultimo ponto.
        bezierCurves.push(curve[curve.length-1]);
        drawControlPolygon(bezierCurves);
    }
}

// redesenhar
function reDraw(){
    console.log("began redraw");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (showPoligonos){
        for (let i = 0; i < curves.length; i++){
            if (i == selectedCurve){
                ctx.strokeStyle="pink";
            } else {
                ctx.strokeStyle="yellow";
            }
            drawControlPolygon(curves[i]);
        }
    }
    if (showPoints){
        for (let i = 0; i < curves.length; i++){
            for (let j = 0; j < curves[i].length; j++){
                if ((j == selectedPoint[selectedCurve]) && (i == selectedCurve)){
                    ctx.strokeStyle="orange";
                } else {
                    ctx.strokeStyle="blue";
                }
                drawPoint(curves[i][j]);
            }
        }
    }
    if (showCurves && (numAvaliacoes > 1)){
        for (let i = 0; i < curves.length; i++){
            if (i == selectedCurve){
                ctx.strokeStyle="green";
            } else {
                ctx.strokeStyle="red";
            }
            drawBezierCurve(curves[i]);
        }
    }
    console.log("finished redraw");
}

// event listeners

// canvas: reDraw é a função principal que vai ser sempre chamada para refletir em tempo real as mudanças

// clique no mouse
canvas.addEventListener("mousedown", function(event){
    clique = true;
    // novo ponto a
    var a = new Point(event.offsetX, event.offsetY);
    if (stateCanvas == 1){
        curves[selectedCurve].push(a);
    } else if (stateCanvas == 2){
        curves[selectedCurve].splice(selectedPoint[selectedCurve], 1, a);
    }
    reDraw();
});

// movimento do mouse
canvas.addEventListener("mousemove", function(event){
    if (clique){
        if (stateCanvas == 2){
            var a = new Point(event.offsetX, event.offsetY);
            curves[selectedCurve].splice(selectedPoint[selectedCurve], 1, a);
        }
    }
    reDraw();
});

// solta o mouse
canvas.addEventListener("mouseup", function(event){
    clique = false;
    reDraw();
    console.log("mouseup");
});

// botões

// adicionar curva
newCurvaBtn.addEventListener("click", function(event){
    if (selectedCurve == -1 || curves[selectedCurve].length > 1){
        stateCanvas = 1;
        var newCurve = [];
        curves.push(newCurve);
        selectedPoint.push(0);
        selectedCurve++;
        legendaText.innerText = "Clique no canvas para adicionar os pontos de controle.";
    } else {
        legendaText.innerText = "Finalize a curva atual antes de começar uma nova.";
    }
});

delCurvaBtn.addEventListener("click", function(event){
    if (curves.length > 0){
        curves.splice(selectedCurve, 1);
        selectedPoint.splice(selectedCurve, 1);
        if (selectedCurve > 0){
            selectedCurve--;
        }
        reDraw();
    } else {
        return;
    }   
});

previousCurveBtn.addEventListener("click", function(event){
    if (selectedCurve > 0){
        selectedCurve--;
        reDraw();
    } else { 
        return;
    }
});

nextCurveBtn.addEventListener("click", function(event){
    if (selectedCurve < curves.length - 2){
        selectedCurve++;
        reDraw();
    } else { 
        return;
    }
});

// add pontos
addPontoBtn.addEventListener("click", function(event){
    stateCanvas = 1;
    legendaText.innerText = "Clique no canvas para adicionar os pontos de controle.";
});

// deletar o ponto selecionado
delPontoBtn.addEventListener("click", function(event){
    if (curves[selectedCurve].length > 0){
        curves[selectedCurve].splice(selectedPoint[selectedCurve], 1);
        selectedPoint.splice(selectedCurve, 1);
        if (curves[selectedCurve].length == 0){
            // remove a curva, pois ela ficou vazia
            curve.splice(selectedCurve, 1);
            selectedPoint.splice(selectedCurve, 1);
            if (selectedCurve > 0){
                selectedCurve--;
            }
        }
        reDraw();
    } else {
        return;
    }
});

movePontoBtn.addEventListener("click", function(event){
    stateCanvas = 2;
    legendaText.innerText = "Arraste os pontos no canvas para reposicioná-los.";
});

previousPontoBtn.addEventListener("click", function(event){
    if (selectedPoint[selectedCurve] > 0){
        selectedPoint[selectedCurve]--;
    } else { 
        return;
    }
    reDraw();
});

nextPontoBtn.addEventListener("click", function(event){
    if (selectedPoint[selectedCurve] < curves[selectedCurve].length - 1){
        selectedPoint[selectedCurve]++;
    } else { 
        return;
    }
    reDraw();
});

// checkboxes

// poligonos
poligonosCheckbox.addEventListener("click", function(event){
    showPoligonos = !showPoligonos;
    reDraw();
});

// pontos
pontosCheckbox.addEventListener("click", function(event){
    showPoints = !showPoints;
    reDraw();
});

// curvas
curvasCheckbox.addEventListener("click", function(event){
    showCurves = !showCurves;
    reDraw();
});

// numero de avaliacoes input
numAvaliacoesInput.addEventListener("keyup", function(event){
    var input = event.target.value;
    numAvaliacoes = parseInt(input);
    reDraw();
});
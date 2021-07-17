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
        for (i = 0; i < grau; i++){
            pontosAux.push(interpolation(pontos[i], pontos[i+1], t));
        }
        return deCasteljau(pontosAux,  t);
    }
}

// elementos da aplicação
// canvas
var canvas = document.getElementsByName("canvas");
var ctx = canvas.getContext("2d");

// legenda
var legendaText = document.getElementsByName("legenda");

// botões - curva
var newCurvaBtn = document.getElementsByName("newCurveBtn");
var delCurvaBtn = document.getElementsByName("delCurveBtn");
var previousCurveBtn = document.getElementsByName("previousCurveBtn");
var nextCurveBtn = document.getElementsByName("nextCurveBtn");

// botões - pontos
var addPontoBtn = document.getElementsByName("addPontoBtn");
var movePontoBtn = document.getElementsByName("movePontoBtn");
var previousPontoBtn = document.getElementsByName("previousPontoBtn");
var nextPontoBtn = document.getElementsByName("nextPontoBtn");

// input e checkboxes
var numAvaliacoesInput = document.getElementsByName("avaliacoes");
var poligonosCheckbox = document.getElementsByName("poligonosCheckbox");
var pontosCheckbox = document.getElementsByName("pontosCheckbox");
var curvasCheckbox = document.getElementsByName("curvasCheckbox");

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
    for (i = 0; i < pontos.length-1; i++){
        drawLine(pontos[i], pontos[i+1]);
    }
}

// desenha a curva
function drawBezierCurve(curve){
    if (curve.length > 2){
        var bezierCurves = [];
        bezierCurves.push(curve[0]);
        // a iteração é até numAvaliações - 2, pois já estão inclusos os pontos inicial e final, que são dados pelo usuário.
        for (i = 1; i <= numAvaliacoes-2; i++){
            bezierCurves.push(deCasteljau(curve, i / numAvaliacoes));
        }
        // esse ultimo push fora do laço é para que ele não fique dando aquela sobrinha, entre a ultima avaliação e o ultimo ponto.
        bezierCurves.push(curve[curve.length-1]);
        drawControlPolygon(bezierCurves);
    }
}

// redesenhar
function reDraw(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (showPoligonos){
        for (i = 0; i < curves.length; i++){
            if (i == selectedCurve){
                ctx.strokeStyle="pink";
            } else {
                ctx.strokeStyle="yellow";
            }
            drawControlPolygon(curves[i]);
        }
    }
    if (showPoints){
        for (i = 0; i < curves.length; i++){
            for (j = 0; j < curves[i].length; j++){
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
        for (i = 0; i < curves.length; i++){
            if (i == selectedCurve){
                ctx.strokeStyle="green";
            } else {
                ctx.strokeStyle="red";
            }
            drawBezierCurve(curves[i]);
        }
    }
}
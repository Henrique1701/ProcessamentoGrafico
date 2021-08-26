PImage mapaNormais;
PImage imagemDifusa;
PImage imagemEspecular;
PImage imagemFinal;

int branco = 255;
int cinza = 167;
int preto = 0;

int controleDifuso[] = {branco,preto,branco};
int controleEspecular[] = {branco,preto,branco};

float r = 255;
float g = 255;
float b = 255;
float posicaoInicialSliders;
float posicaoR;
float posicaoG;
float posicaoB;
boolean pressionandoR = false;
boolean pressionandoG = false;
boolean pressionandoB = false;
float deslocamentoR = 0;
float deslocamentoG = 0;
float deslocamentoB = 0;

int fonteBotaoComponente = 30;
int fonteBotaoCores = 25;

PVector direcaoVista = new PVector(0,1,1);
PVector direcaoLuz;
color corDaLuz;
float brilho;
float coordX, coordY;

void setup() {
  background(0);
  size(800,800);
  imagemDifusa = loadImage("./Imagens/char1_d.png");
  imagemEspecular = loadImage("./Imagens/char1_s.png");
  mapaNormais = loadImage("./Imagens/char1_n.png");
  brilho = 1;
  corDaLuz = color(255,255,255,255);
  direcaoLuz = new PVector(-1,0,1).normalize();
  coordX = width/2.0 - imagemDifusa.width/2.0;
  coordY = height/2.0 - imagemDifusa.height/2.0;
  posicaoInicialSliders = width/2+80;
  posicaoR = posicaoInicialSliders + r;
  posicaoG = posicaoInicialSliders + g;
  posicaoB = posicaoInicialSliders + b;
}

void draw() {
  background(0);
  botoes();
  sliders();
  corDaLuz = color (r,g,b);
  direcaoLuz = new PVector(mouseX - width/10, mouseY - height/10, 0.1).normalize();
  imagemFinal = createImage(imagemDifusa.width, imagemDifusa.height, ARGB);
  renderizarImagem();
  image(imagemFinal,coordX,coordY);
}

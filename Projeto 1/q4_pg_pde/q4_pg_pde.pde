float alpha = 0; //<>//
float w = PI/240; //rotação de 180° em 4s

//coordenadas iniciais
float px = -20;
float py = 0;

//coordenadas do centro que são modificadas qnd passa no 0x
float centrox = 0;
float centroy = 0;
int i = 1;

void pontos() {
  strokeWeight(10);
  stroke(255,0,0);
}

void eixox() {
  stroke(0,0,255);
}

void eixoy() {
  stroke(0,255,0);
}

void initialSetup() {
  translate(400,400);
  strokeWeight(1);
  stroke(0);
  eixox();
  line(-400,0,400,0);
  eixoy();
  line(0,400,0,-400);
  scale(1,-1);
}

void setup() {
  size(800,800);
  frameRate(60);
}

void draw(){
  initialSetup();
  
  if(alpha >= PI){ //alpha >= 180°, o centro vira o  ponto inicial x e o ponto inicial x é alterado é alterado
    alpha = 0;
    centrox = px;
    px += -20*pow(-2,i);
    i++;
  }
  
  translate(centrox, centroy); //translada o centro para o lado, para aumentar o raio do semicirculo
  rotate(alpha); //rotaciona o ponto
  translate(-centrox, -centroy);
  pontos();
  point(px, py);
  alpha += w; //incrementa o w para que aconteça a rotação
}

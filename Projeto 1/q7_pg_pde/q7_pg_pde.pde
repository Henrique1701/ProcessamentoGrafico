int mov = 1;

// controle do movimento atual do y.
float y = 100; 

// pontos relevantes da questao
float ax = 400;
float ay = 100;
float az = 0;

float bx = -100;
float by = 50/3;
float bz = 500;

float cx = 0;
float cy = 0;
float cz = 600;

float dx = 100;
float dy = -50/3;
float dz = 500;

float ex = -400;
float ey = -100;
float ez = 0;

// velocidades
float w1 = PI/360;
float w2 = PI/120;
float w3 = w1;

float v1 = 0.46296;
float v2 = 0.27778;
float v3 = v1;

// raio da esfera
float r = 40;

// 
float alpha = 0;

void setup() {
  size(1000, 1000, P3D);
  frameRate(60);
}

void config(){
  background(220);
  translate(500, 700, 0);
   
  // Deixar no angulo de visualizacao correto
  rotateZ(-PI/2);
  rotateY(PI/2);
  scale(-1, 1, 1);
  rotateZ(-PI/6);

  // eixos x, y e z
  strokeWeight(2);
  stroke(255, 0, 0);
  line(0, 0, 0, 500, 0, 0); // x | red
  stroke(0, 255, 0);
  line(0, 0, 0, 0, 500, 0); // y | green
  stroke(0, 0, 255);
  line(0, 0, 0, 0, 0, 500); // z | blue
}

void esfera(float x, float y, float z, float raio){
   strokeWeight(raio);
   stroke(0); // preto
   point(x, y, z);
}

void draw() {
  config();
  if (mov == 1){
    mov1();
  }
  else if (mov == 2){
    mov2();
  }
  else if (mov == 3){
    mov3(); 
  }
}

void mov1(){
  translate(400, y, 500);
  rotateY(alpha);
  translate(-400, -y, -500);
  esfera(ax, y, az, r);
  
  if (alpha < PI/2){
    alpha = alpha + w1;
    y = y - v1;
  } else {
    mov = 2;
    alpha = w1;
  }
}

void mov2(){
  translate(0, y, 500);
  rotateY(alpha);
  translate(0, -y, -500);
  // Aqui é preciso usar o valor atualizado do y pro movimento não ficar "quebrado"
  esfera(bx, y, bz, r);
  
  if (alpha < PI){
    alpha = alpha + w2;
    y = y - v2;
  } else {
    mov = 3;
    alpha = w2;
  }
}

void mov3(){
  translate(-400, -y, 500);
  rotateY(alpha);
  translate(400, y, -500);
  // Aqui é preciso usar o valor atualizado do y pro movimento não ficar "quebrado"
  esfera(dx, y, dz, r);
  
  if (alpha < PI/2){
    alpha = alpha + w3;
    y = y - v3;
  } else {
    mov = 0; //para
    alpha = 0;
  }
}

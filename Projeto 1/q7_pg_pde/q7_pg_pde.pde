int mov = 1;

// coordenadas da esfera (centro). inicializa no ponto A
float cx = 400;
float cy = 100;
float cz = 0;
// raio da esfera
float r = 20;

// 
float alpha = 0;

void setup() {
  size(1000, 1000, P3D);
  frameRate(60);

}

void draw() {
  start();
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

void start(){
  background(220);
  translate(400, 400, 0);
  rotateX(PI/2); // rotate 20º para poder ver as 3 coodenadas
  rotateZ(-PI/2);
  rotateY(-PI/10);
   scale(-1, 1, 1);
  // eixos x, y e z
  stroke(255, 0, 0);
  line(0, 0, 0, 400, 0, 0); 
  stroke(0, 255, 0);
  line(0, 400, 0, 0, 0, 0);  
  stroke(0, 0, 255);
  line(0, 0, 400, 0, 0, 0);
  
}

void mov1(){
  translate(0, 0, 400);
  rotateY(alpha);
  translate(0, 0, -400); // desfaz o translate anterior
  sphere(r);
  if (alpha <= PI/2){
    alpha+= PI/360;
  } else {
    mov = 2;
    alpha = 0;
  }
}

void mov2(){
  translate(0, 0, 400);
  rotateY(alpha);
  translate(0, 0, -400); // desfaz o translate anterior
  sphere(r);
  if (alpha <= PI){
    alpha+= PI/120;
  } else {
    mov = 3;
    alpha = 0;
  }
}

void mov3(){
  translate(0, 0, 400);
  rotateY(alpha);
  translate(0, 0, -400); // desfaz o translate anterior
  sphere(r);
  if (alpha <= PI/2){
    alpha+= PI/360;
  } else {
    mov = 0;
    alpha = 0;
  }
}

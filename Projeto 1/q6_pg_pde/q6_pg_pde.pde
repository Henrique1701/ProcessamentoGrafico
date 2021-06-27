float theta = 0;
float alpha = 0;

void settings() {
  System.setProperty("jogl.disable.openglcore", "true");
  size(800, 800, P3D);
}

void setup() {
  PGraphicsOpenGL pg = (PGraphicsOpenGL)g;
  println(PGraphicsOpenGL.OPENGL_VENDOR);
  println(PGraphicsOpenGL.OPENGL_RENDERER);
  println(PGraphicsOpenGL.OPENGL_VERSION);
  println(PGraphicsOpenGL.GLSL_VERSION);
  frameRate(60);
  rectMode(CENTER);
}

void draw() {
  translate(400,400, 0);
  scale(1,-1,1);
  background(255);
  rotateX(PI/1.8);
  //rotateY(PI/10);
  rotateZ(PI);
  rotateZ(PI/4);
  rotateY(PI); 
  rotateZ(-PI/4);
  rotateY(PI/10); 
  rotateZ(PI/8);
  //essas primeiras rotacoes foram apenas para mudar a perspectiva do espaço, talvez alguem queira mudar para deixar mais parecido com a imagem no enunciado
  
  stroke(255, 0, 0);
  line(0,0,0,300,0,0);
  stroke(0, 255, 0);
  line(0,0,0,0,300,0);
  stroke(0, 0, 255);
  line(0,0,0,0,0,300);
  stroke(0);
  strokeWeight(5);
  circle(0,0,5);
  rotateX(PI/3);
  fill(255);
  circle(100, 100, 200);
  point(100,100,0);
  noFill();
  rect(100, 100, 200, 200);
  translate(100, 100, 0);
  rotateZ(theta);
  translate(0, -100, 25);
  rotateX(PI/2);
  rotateZ(alpha);
  circle(0, 0, 50);
  //fill(255, 0,0);
  stroke(255,0,0);
  circle(0, 25, 5);
  stroke(0);
  noFill();
  theta += PI/120;
  alpha -= PI/30;
}

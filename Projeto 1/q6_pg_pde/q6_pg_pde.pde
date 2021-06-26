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
  background(200);
  strokeWeight(4);
  circle(0,0,5);
  rotateX(PI/3);
  circle(100, 100, 200);
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

float theta = 0;
float alpha = 0;

//leiam o draw() de baixo para cima, e perdoem meu analfabetismo 

void settings() {
  System.setProperty("jogl.disable.openglcore", "true");
  size(800, 800, P3D);
}

//ignorem as configuracoes, minha maquina quem pediu
void setup() {
  PGraphicsOpenGL pg = (PGraphicsOpenGL)g;
  println(PGraphicsOpenGL.OPENGL_VENDOR);
  println(PGraphicsOpenGL.OPENGL_RENDERER);
  println(PGraphicsOpenGL.OPENGL_VERSION);
  println(PGraphicsOpenGL.GLSL_VERSION);
  frameRate(60);
  rectMode(CENTER); //para as coordenadas passadas no desenho do retangulo indiquem seu centro
}

void draw() {
  translate(400,400, 0);
  //ajeitando a direcao do eixo y
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
  //como elas serão as ultimas transformações, não alteram o movimento
  
  stroke(255, 0, 0); //linha do eixo x
  line(0,0,0,300,0,0);
  stroke(0, 255, 0); //linha do eixo y
  line(0,0,0,0,300,0);
  stroke(0, 0, 255); //linha do eixo z
  line(0,0,0,0,0,300);
  stroke(0); // linhas pretas
  strokeWeight(5); //linhas mais espessas
  circle(0,0,5);//representar a origem
  //rotaciona os objetos em 60 graus em torno do eixo x
  rotateX(PI/3);
  //desenha o circulo maior pintado de branco com um ponto no meio
  fill(255);
  circle(100, 100, 200);
  point(100,100,0);
  //desenha o retângulo transparente onde o circulo maio estará inscrito
  noFill();
  rect(100, 100, 200, 200);
  //move o circulo menor para onde o circulo maior estaria se estivesse conti no plano XY
  //mas com centro fora da origem. centro em (100,100,0)
  translate(100, 100, 0);
  //roda em torno do circulo maior, se este tivesse centro na origem tambem
  rotateZ(theta);
  //move o circulo menor para ele ficar "em pé" em cima de onde
  //seria o circulo maior se ele tivesse origem no meio e fosse desenhado em XY
  translate(0, -100, 25);
  //traz o desenho do plano XY para o plano YZ, ainda com o centro na origem
  rotateX(PI/2);
  //como o circulo menor foi desenhado no centro do plano XY, essa 
  //rotacao afeta apenas da bolinha vermelha
  rotateZ(alpha);
  
  //todos os desenhos a seguir são feitos no plano XY
  //desenhando o circulo menor pintado de branco com um ponto no meio
  fill(255);
  circle(0, 0, 50);
  point(0,0);
  
  //desenhando o ponto vermelho que indica o rolamento co circulo menor
  stroke(255,0,0);
  strokeWeight(8);//para o circulo ficar maiorzinho
  point(0, 25);
  //voltando para as configurações de desenho que tava antes
  strokeWeight(5);
  stroke(0);
  noFill();
  
  theta += PI/120; //velocidade da rotacao do circulo menor em torno maior
  alpha -= PI/30; //velocidade da rotacao do circulo menor em torno de si mesmo
}

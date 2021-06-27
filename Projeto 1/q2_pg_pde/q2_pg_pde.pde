float xOmbro;
float yOmbro;

float xCotovelo;
float yCotovelo;

float targetAngle = -0.523; //Angulo em que o antebraco fica na horizontal
float currentAngle = 0;
float vw = -0.004; //velocidade angular

float r = 7;
int s;

void setup() {
  size(800, 600);
  
  xOmbro = width/2;
  yOmbro = height/2;
  
  xCotovelo = xOmbro;
  yCotovelo = yOmbro + 100;
  
  s = second();
  
}

void draw() {
  background(255);
  
  //s = second();
  
  if (currentAngle <= targetAngle){
    vw = 0;
  }
  
  currentAngle += vw;
  
  // braco
  stroke(0);
  circle(xOmbro, yOmbro, r);
  
  translate(xOmbro, yOmbro); 
  rotate(currentAngle);
  
  line(0, 0, 0, 100);
  circle(0, 100, r);

  // ante-braco
  translate(-xOmbro, -yOmbro);
  translate(xCotovelo, yCotovelo); 
  rotate(2 * currentAngle);
  
  line(0, 0, 0, 150);
  circle(0, 150, r);
  
  //Calcula tempo decorrido desde o inicio da execucao
  //(se executar muito perto da virada do minuto, vai dar um valor negativo mesmo)
  print(second() - s);
  print("\n");
  
}

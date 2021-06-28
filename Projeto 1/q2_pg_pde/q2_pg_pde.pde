float xOmbro;
float yOmbro;

float xCotovelo;
float yCotovelo;

// define o angulo em que o braco deve parar
float targetAngle = -0.523; //Angulo em que o antebraco fica na horizontal
// define o angulo inicial
float currentAngle = 0;
float vw = -0.004; //velocidade angular

//raio das bolinhas que foram colocadas para ilustrar o ombro, cotovelo e mao
float r = 7;
int s;

void setup() {
  size(800, 600);
  
  // inicializa a posicao x e y do ombro no centro do espaco 
  xOmbro = width/2;
  yOmbro = height/2;
  
  // inicializa a posicao do cotovelo 100 unidades abaixo do ombro
  xCotovelo = xOmbro;
  yCotovelo = yOmbro + 100;
  
  s = second();
  
}

void draw() {
  background(255);
  
  // condicao de parada: Se o angulo atual chegar no que foi definido como alvo, a velocidade angular fica zerada e nao ha mais movimento
  // estou usando o braco como referencial, mas poderia ser usado o antebraco tambem, se fizer as modificacoes necessarias
  if (currentAngle <= targetAngle){
    vw = 0;
  }
  
  // angulo atual vai ser ele mesmo + a velocidade angular. A cada frame o angulo atual aumenta um pouco, produzindo o movimento
  currentAngle += vw;
  
  // braco
  stroke(0);
  circle(xOmbro, yOmbro, r);
  
  // translada o ponto de origem para o mesmo ponto onde esta o ombro, dessa forma a rotacao do braco vai ser em relacao ao ombro
  translate(xOmbro, yOmbro); 
  rotate(currentAngle);
  
  line(0, 0, 0, 100);
  circle(0, 100, r);

  // ante-braco
  // translada de volta para o ponto de origem
  translate(-xOmbro, -yOmbro);
  // translada agora para o cotovelo, para que a rotacao do antebraco seja em relacao a esse ponto
  translate(xCotovelo, yCotovelo); 
  rotate(2 * currentAngle);
  
  line(0, 0, 0, 150);
  circle(0, 150, r);
  
  //Calcula tempo decorrido desde o inicio da execucao
  //(se executar muito perto da virada do minuto, vai dar um valor negativo mesmo)
  print(second() - s);
  print("\n");
  
}

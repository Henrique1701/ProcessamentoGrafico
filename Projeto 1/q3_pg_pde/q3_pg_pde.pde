float x = 100;
float y = 0;
float alpha = 0;

void setup() {
  size(800, 800);
  frameRate(60);
}

void setUpCoordinateSystem() {
  // Translada a origem para o centro da tela
  translate(width/2, height/2);
  
  // Configura linhas de referência
  stroke(0);
  strokeWeight(2);
  line(0, -350, 0, 350);
  line(-350, 0, 350, 0);
  
  // Inverte o sentido da coordenada y
  scale(1,-1);
}

void draw() {
  setUpCoordinateSystem();
  
  // Configura a aparência da partícula
  stroke(0, 0, 150);
  strokeWeight(4);
  
  // Rotaciona o sistema em alpha graus
  rotate(alpha);
  
  // Calcula qual deverá ser a próxima possição x na partícula
  float newX = x * (1 + alpha/PI);
  
  // Verifica a particula chegou no ponto (-200, 0)
  if (newX <= 200) {
    // Adiciona um ponto na nova coordenada
    point(newX, y);
    alpha += PI/240;
  }
}

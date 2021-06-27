float x, y;
float xSpeed, ySpeed;

void setup(){
  size(640, 480);
  
  // iniciliza a posicao inicial da bola
  x = 0;
  y = 100;
  
  // inicializa a velocidade inicial da bola
  xSpeed = 5;
  ySpeed = 3;
}

void draw(){
  // cria o background e o retangulo vermelho que vai ser o "chao"
  background(155);
  fill(#FF0000); //red
  rect(0, 315, width, 200);
  
  // cria a bolinha na posicao x e y e raio = 30. x e y vao ser alterados a cada iteracao/frame
  fill(#0085ca); //blue 
  circle(x, y, 30);
  
  // define os novos x e y a serem usados na proxima iteracao
  x = x + xSpeed;
  y = y + ySpeed;
  
  // aceleracao da gravidade, assim como foi pedido na questao
  ySpeed = ySpeed + 0.5f;
  
  // aqui ocorrem os checks para garantir que a bola nao saia do espaco delimitado
  
  if(x >= width){
    // checa se a bola passou da lateral direita. caso positivo, inverte a velocidade no eixo x
    xSpeed = -xSpeed;
  }else if(x <= 0){
    // checa se a bola passou da lateral esquerda. caso positivo, inverte a velocidade no eixo x
    xSpeed = -xSpeed;
  }
  
  if(y >= 300){
    // checa se a bola passou do "chao". caso positivo, inverte a velocidade no eixo y, ja com aceleracao e posiciona a bola exatamente no limite do chao
    ySpeed = -ySpeed + 0.5f;
    y = 300;
  }else if(y <= 0){
    // checa se a bola passou do "teto". caso positivo, inverte a velocidade no eixo y.
    // como a propria gravidade desacelera a bola, esse estado nunca e atingido, mas fizemos o check mesmo assim
    ySpeed = -ySpeed;
  }
}

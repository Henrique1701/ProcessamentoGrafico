void botoes() {
  stroke(controleDifuso[0]);
  strokeWeight(1);
  fill(controleDifuso[1]);
  rect(25,30,width/4-4,40, 8,8,8,8);
  fill(controleDifuso[2]);
  textSize(fonteBotaoComponente);
  textAlign(CENTER, CENTER);
  text("Difuso", width/8+25,48);

  stroke(controleEspecular[0]);
  strokeWeight(1);
  fill(controleEspecular[1]);
  rect(width/4+35,30,width/4-4,40, 8,8,8,8);
  fill(controleEspecular[2]);
  textSize(fonteBotaoComponente);
  textAlign(CENTER, CENTER);
  text("Especular", 3*width/8+35,48);
}

void sliders() {
  stroke(255);
  strokeWeight(2);
  line(posicaoInicialSliders, 30, posicaoInicialSliders+255, 30);
  line(posicaoInicialSliders, 50, posicaoInicialSliders+255, 50);
  line(posicaoInicialSliders, 70, posicaoInicialSliders+255, 70);
  
  stroke(0);
  strokeWeight(1);
  
  fill(200, 50, 50);
  circle(posicaoR, 30, 20);

  fill(50, 200, 50);
  circle(posicaoG, 50, 20);
  
  fill(50, 50, 200);
  circle(posicaoB, 70, 20);
}

void mouseClicked() {
  if(((mouseX >= 25) && (mouseX <= width/4+23))&& ((mouseY >= 30) && (mouseY <= 70))) {
    // Clicou no botão "Difuso"
    if (controleDifuso[1] == branco) { 
       controleDifuso[0] = cinza;
       controleDifuso[1] = cinza;
       controleDifuso[2] = branco;
    } else {
      controleDifuso[0] = branco;
      controleDifuso[1] = branco;
      controleDifuso[2] = preto;
    }
  } else if (((mouseX >= width/4+35)&&(mouseX <= width/2+25))&&((mouseY >= 30)&&(mouseY <= 70))) {
    // Clicou no botão "Especular"
    if (controleEspecular[1] == branco) {
       controleEspecular[0] = cinza;
       controleEspecular[1] = cinza;
       controleEspecular[2] = branco;
    } else {
      controleEspecular[0] = branco;
      controleEspecular[1] = branco;
      controleEspecular[2] = preto;
    }
  }
}

void mousePressed() {
  // Método que é chamado sempre que o botão do mouse é pressionado
  // E verifica se está pressionando algum dos sliders
  if(mouseX >= posicaoR-10 && mouseX <= posicaoR+10 && mouseY >= 20 && mouseY <= 40) {
    pressionandoR = true;
    deslocamentoR = mouseX - posicaoR;
  } else if (mouseX >= posicaoG-10 && mouseX <= posicaoG+10 && mouseY >= 40 && mouseY <= 60) {
    pressionandoG = true;
    deslocamentoG = mouseX - posicaoG;
  } else if (mouseX >= posicaoB-10 && mouseX <= posicaoB+10 && mouseY >= 60 && mouseY <= 80) {
    pressionandoB = true;
    deslocamentoB = mouseX - posicaoB;
  }
}

void mouseReleased() {
  // Método que é chamado toda vez que para de pressionar o botão do mouse
  pressionandoR = false; 
  pressionandoG = false;
  pressionandoB = false;
}

void mouseDragged() {
  // Método chamado toda vez que mexe o mouse com o botão pressionado
  // E verifica se precisa atualiar a posição de algum slider
  if (pressionandoR) {
    float novaPosicao = mouseX-deslocamentoR;
    if (novaPosicao > posicaoInicialSliders && novaPosicao < posicaoInicialSliders+255) {
      posicaoR = novaPosicao;
      r = posicaoR - posicaoInicialSliders;
    }
  } 
  else if (pressionandoG) {
    float novaPosicao = mouseX-deslocamentoG;
    if (novaPosicao > posicaoInicialSliders && novaPosicao < posicaoInicialSliders+255) {
      posicaoG = novaPosicao;
      g = posicaoG - posicaoInicialSliders;
    }
  }
  else if (pressionandoB) {
    float novaPosicao = mouseX-deslocamentoB;
    if (novaPosicao > posicaoInicialSliders && novaPosicao < posicaoInicialSliders+255) {
      posicaoB = novaPosicao;
      b = posicaoB - posicaoInicialSliders;
    }
  }
}

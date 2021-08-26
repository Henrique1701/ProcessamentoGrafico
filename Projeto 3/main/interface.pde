void botoes() {
  stroke(controleDifuso[0]);
  strokeWeight(4);
  fill(controleDifuso[1]);
  rect(2,2,width/4-4,40);
  fill(controleDifuso[2]);
  textSize(fonteBotaoComponente);
  textAlign(CENTER, CENTER);
  text("Difuso", width/8,20);

  stroke(controleEspecular[0]);
  strokeWeight(4);
  fill(controleEspecular[1]);
  rect(width/4+2,2,width/4-4,40);
  fill(controleEspecular[2]);
  textSize(fonteBotaoComponente);
  textAlign(CENTER, CENTER);
  text("Especular", 3*width/8,20);
}

void sliders() {
  stroke(255);
  strokeWeight(4);
  line(posicaoInicialSliders, 10, posicaoInicialSliders+255, 10);
  line(posicaoInicialSliders, 30, posicaoInicialSliders+255, 30);
  line(posicaoInicialSliders, 50, posicaoInicialSliders+255, 50);
  
  stroke(0);
  strokeWeight(1);
  
  fill(200, 50, 50);
  circle(posicaoR, 10, 20);

  fill(50, 200, 50);
  circle(posicaoG, 30, 20);
  
  fill(50, 50, 200);
  circle(posicaoB, 50, 20);
}

void mouseClicked() {
  if(((mouseX >= 2) && (mouseX <= width/4-2))&& ((mouseY >= 2) && (mouseY <= 40))) {
    // Clicou no botão "Difuso"
    if (controleDifuso[1] == cinza) { 
       controleDifuso[0] = branco;
       controleDifuso[1] = preto;
       controleDifuso[2] = branco;
    } else {
      controleDifuso[0] = preto;
      controleDifuso[1] = cinza;
      controleDifuso[2] = preto;
    }
  } else if (((mouseX >= width/4+2)&&(mouseX <= width/2-2))&&((mouseY >= 2)&&(mouseY <= 40))) {
    // Clicou no botão "Especular"
    if (controleEspecular[1] == cinza) {
       controleEspecular[0] = branco;
       controleEspecular[1] = preto;
       controleEspecular[2] = branco;
    } else {
      controleEspecular[0] = preto;
      controleEspecular[1] = cinza;
      controleEspecular[2] = preto;
    }
  }
}

void mousePressed() {
  // Método que é chamado sempre que o botão do mouse é pressionado
  // E verifica se está pressionando algum dos sliders
  if(mouseX >= posicaoR-10 && mouseX <= posicaoR+10 && mouseY >= 0 && mouseY <= 20) {
    pressionandoR = true;
    deslocamentoR = mouseX - posicaoR;
  } else if (mouseX >= posicaoG-10 && mouseX <= posicaoG+10 && mouseY >= 20 && mouseY <= 40) {
    pressionandoG = true;
    deslocamentoG = mouseX - posicaoG;
  } else if (mouseX >= posicaoB-10 && mouseX <= posicaoB+10 && mouseY >= 40 && mouseY <= 60) {
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

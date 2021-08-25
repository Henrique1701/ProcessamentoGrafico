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
  
  //cores
  stroke(controleVermelho);
  strokeWeight(4);
  fill(r,0,0);
  circle(7*width/12+20,22,40);
  fill(preto);
  textSize(fonteBotaoCores);
  textAlign(CENTER, CENTER);
  text('R',7*width/12+20,22);
  
  stroke(controleVerde);
  strokeWeight(4);
  fill(0,g,0);
  circle(9*width/12+20,22,40);
  fill(preto);
  textSize(fonteBotaoCores);
  textAlign(CENTER, CENTER);
  text('G',9*width/12+20,22);
  
  stroke(controleAzul);
  strokeWeight(4);
  fill(0,0,b);
  circle(11*width/12+20,22,40);
  fill(preto);
  textSize(fonteBotaoCores);
  textAlign(CENTER, CENTER);
  text('B',11*width/12+20,22);
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
  } else if ((((abs(mouseX) - (7*width/12+20)) <= 22)&&(abs(mouseY - 22) <= 22))) {
    // Clicou no botão "R"
    if (controleVermelho == preto) {
      controleVermelho = branco;
    } else {
      controleVermelho = preto;
    }
  } else if ((((abs(mouseX) - (9*width/12+20)) <= 22)&&(abs(mouseY - 22) <= 22))) {
    // Clicou no botão "G"
    if (controleVerde == preto) {
      controleVerde = branco;
    } else {
      controleVerde = preto;
    }
  } else if ((((abs(mouseX) - (11*width/12+20)) <= 22)&&(abs(mouseY - 22) <= 22))) {
    // Clicou no botão "B"
    if (controleAzul == preto) {
      controleAzul = branco;
    } else {
      controleAzul = preto;
    }
  }
}

void keyPressed() {
  if (key == CODED) {
    if (controleVermelho == branco) {
      // Controla a intensidade da luz vermelha
      if (keyCode == UP) {
         r = min(r - 5,255);
      } else if (keyCode == DOWN) {
        r = max(r - 5,0);
      }
    }
    
    if (controleVerde == branco) {
      // Controla a intensidade da luz verde
      if (keyCode == UP) {
         g = min(g - 5,255);
      } else if (keyCode == DOWN) {
        g = max(g - 5,0);
      }
    }
    
    if (controleAzul == branco) {
      // Controla a intensidade da luz azul
      if (keyCode == UP) {
         b = min(b - 5,255);
      } else if (keyCode == DOWN) {
        b = max(b - 5,0);
      }
    }
    
  }
}

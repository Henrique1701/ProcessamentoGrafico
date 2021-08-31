PVector refletir(PVector incidente, PVector normal) {
  PVector refletido = normal.normalize();
  return incidente.sub(refletido.mult(2*incidente.dot(refletido)));
}

color capturarPixel(PImage imagem, int pixelX, int pixelY) {
  return imagem.pixels[pixelY*imagem.width + pixelX];
}

color calcularComponenteDifusa(color difusa, color normal) {
  color componenteDifusa;
  PVector normalNormalizado = new PVector(red(normal), green(normal), blue(normal)).normalize();
  float proporcaoDifusa = max(0, normalNormalizado.dot(direcaoLuz));
  componenteDifusa = color(red(difusa)*proporcaoDifusa, green(difusa)*proporcaoDifusa, blue(difusa)*proporcaoDifusa, alpha(difusa));
  componenteDifusa = iluminarCor(componenteDifusa);
  return componenteDifusa;
}

color calcularComponenteEspecular (color especular, color normal) {
  color componenteEspecular;
  PVector normalNormalizado = new PVector(red(normal), green(normal), blue(normal)).normalize();
  PVector incidente = PVector.mult(direcaoLuz, -1);
  PVector refletido = refletir(incidente, normalNormalizado);
  float proporcaoEspecular = pow(max(0, direcaoVista.dot(refletido)), brilho);
  componenteEspecular = color(red(especular)*proporcaoEspecular, green(especular)*proporcaoEspecular, blue(especular)*proporcaoEspecular, alpha(especular));
  componenteEspecular = iluminarCor(componenteEspecular);
  return componenteEspecular;
}

color juntarComponentes(color corDifusa, color corEspecular) {
  color corFinal;
  float r = (red(corDifusa) + red(corEspecular));
  float g = (green(corDifusa) + green(corEspecular));
  float b = (blue(corDifusa) + blue(corEspecular));
  corFinal = color(r,g,b, alpha(corDifusa));
  return corFinal;
}

color iluminarCor(color cor) {
  color novaCor;
  float novoVermelho = red(cor)*red(corDaLuz)/255.0;
  float novoVerde = green(cor)*green(corDaLuz)/255.0;
  float novoAzul = blue(cor)*blue(corDaLuz)/255.0;
  novaCor = color(novoVermelho, novoVerde, novoAzul, alpha(cor));
  return novaCor;
}

void renderizarImagem(){
  for (int y = 0; y < imagemDifusa.height; y++) {
    for (int x = 0; x < imagemDifusa.width; x++) {
      color normal = capturarPixel(mapaNormais, x, y);
      color difusa = capturarPixel(imagemDifusa, x, y);
      color especular = capturarPixel(imagemEspecular, x, y);
      
      color diffuseCol = calcularComponenteDifusa(difusa,normal);
      color specularCol = calcularComponenteEspecular(especular,normal);
      
      if((controleDifuso[1] == branco) & (controleEspecular[1] == branco)) {
        imagemFinal.pixels[y*imagemDifusa.width + x] = juntarComponentes(diffuseCol, specularCol);
      } else if ((controleDifuso[1] == branco) & (controleEspecular[1] == cinza)) {
        imagemFinal.pixels[y*imagemDifusa.width + x] = diffuseCol;
      } else if ((controleDifuso[1] == cinza) & (controleEspecular[1] == branco)) {
        imagemFinal.pixels[y*imagemDifusa.width + x] = specularCol;
      } else {
        imagemFinal.pixels[y*imagemDifusa.width + x] = normal;
      }

      
    }
  }
}

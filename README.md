# ProcessamentoGrafico

### Estruturas
  
  
1. - [x] Ponto(x1, x2, x3) Melissa 
2. - [x] Vetor(x1, x2 x3) Evaldo
3. - [x] Segmento(ponto1, ponto2) Igor
4. - [x] Reta(ponto, vetorDiretor) Mateus
5. - [x] Plano(ponto, vetorNormal) Henrique
6. - [x] Esfera(centro, raio) Melissa
7. - [x] Triangulo(ponto1, ponto2, ponto3) Evaldo
8. - [x] Base(v1, v2, v3)  Igor

### Funções

1. - [x] produtoEscalar(vetor1, vetor2) => n; Henrique
2. - [x] norma(vetor) => n; Mateus
3. - [x] normalize(vetor) => vetorNormalizado; Igor
4. - [x] cosseno(vetor1, vetor2) => angulo; Evaldo
5. - [x] projecao(vetor1, vetor2) => vetor3; Melissa
6. - [x] produtoVetorial(vetor1, vetor2) => vetor3; Henrique
7. - [x] reflexao(vetor1, vetor2) => vetor3; Mateus
8. - [x] saoParalelos(vetor1, vetor2) => boolean; Igor
7. - [x] saoOrtogonais(vetor1, vetor2) => boolean; Evaldo
8. - [x] eLI([vetor1, ..., vetorn]) => boolean; Melissa

### Objetos

1. - [x] diretor(reta) => vetor; Melissa
2. - [x] normal(plano) => vetor; Evaldo
3. - [x] eParalelo(vetor, reta) => boolean; Igor
4. - [x] eOrtogonal(vetor, plano) => boolean; Mateus
5. - [x] projecao(vetor, reta) => vetorProjetado; Henrique
6. - [x] projecao(vetor, plano) => vetorProjetado; Melissa
7. - [x] componenteOrtogonal(vetor, plano) => vetor; Evaldo
8. - [x] saoComplementosOrtogonais(reta, plano) => boolean; Igor
9. - [x] saoComplementosOrtogonais(plano, reta) => boolean; Mateus
10. - [x] formaCartesiana(plano) => [a,b,c,d]  Henrique
11. - [x] formaCartesiana(reta) => [[a,b,c,d],[e,f,g,h]]  Melissa

### Interseções

1. - [X] interseção(reta1, reta2) => objeto; Henrique
2. - [x] interseção(reta, plano) => objeto; Mateus
3. - [x] interseção(reta, esfera) => objeto; Igor
4. - [ ] interseção(reta, triangulo) => objeto; Evaldo
5. - [ ] interseção(plano1, plano2) => objeto; Melissa

### Base:

1. - [x] ortogonalize(base) => (baseOrtogonalizada); Henrique
2. - [x] mudeBase(vetor, base) => [x, y, z]; Mateus
3. - [x] REMOVIDA! mudeBase([x1, y1, z1], base1, base2) => [x2, y2, z2]; Igor

### Transformações Lineares

1. - [x] (Junto da outra rotação)rotação(vetor, ângulo, sentido) => vetorRotacionado; Melissa
2. - [x] rotação(vetor, ângulo, sentido, reta) => vetor; Evaldo
3. - [ ] reflexão(vetor, vetorNormal) => vetor;  Igor
4. - [x] reflexão(vetor, vetorDiretor) => vetorRefletido; Mateus
5. - [x] reflexão(vetor) => vetorRefletido; Henrique
6. - [x] cisalhamento(vetor, eixos, fator) => vetorCisalhado; Melissa
7. - [x] cisalhamento(vetor, eixos, fator1, fator2) => vetorCisalhado, Evaldo
8. - [x] deformação(vetor, fatorX, fatorY, fatorZ) => vetorDeformado;  Igor

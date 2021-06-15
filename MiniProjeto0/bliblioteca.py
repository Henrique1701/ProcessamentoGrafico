import math

#As estruturas básicas precisam ser classes de acordo com as especificações. Aí o resto faz por metodo mesmo.

#ESTRUTURAS
class Ponto:
  def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
    
  def getPonto(self):
    return self.x, self.y, self.z
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getZ(self):
    return self.z

class Vetor:
  def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
    
  def getVetor(self):
    return self.x, self.y, self.z
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getZ(self):
    return self.z

class Segmento:
	def __init__(self, ponto1, ponto2):
		self.ponto1 = ponto1;
		self.ponto2 = ponto2;

	def getSegmento(self):
		return self.ponto1.getPonto(), self.ponto2.getPonto()
	def getPonto1(self):
		return self.ponto1.getPonto()
	def getPonto2(self):
		return self.ponto2.getPonto()   
  
class Reta:
  def __init__(self, ponto, vetordiretor):
      self.ponto = ponto
      self.vetordiretor = vetordiretor

class Plano:
  def __init__(self, ponto: Ponto, vetorNormal: Vetor) -> None:
      self.ponto = ponto
      self.vetorNormal = vetorNormal

  def getPonto(self):
    return self.ponto

  def getVetorNormal(self):
    return self.vetorNormal

class Esfera:
  def __init__(self, ponto, raio):
      self.ponto = ponto 
      self.raio = raio 

  def getEsfera(self):
    return self.ponto.getPonto(), self.raio
  def getCentro(self):
    return self.ponto.getPonto()
  def getRaio(self):
    return self.raio

class Triangulo:
  def __init__(self, ponto1: Ponto, ponto2: Ponto, ponto3: Ponto):
      self.ponto1 = ponto1
      self.ponto2 = ponto2
      self.ponto3 = ponto3

  def getTriangulo(self):
    return self.ponto1.getPonto(), self.ponto2.getPonto(), self.ponto3.getPonto()
  def getPonto1(self):
    return self.ponto1.getPonto()
  def getPonto2(self):
    return self.ponto2.getPonto() 
  def getPonto3(self):
    return self.ponto3.getPonto()

class Base: 
	def __init__(self, vetor1, vetor2, vetor3):
		self.vetor1 = vetor1
		self.vetor2 = vetor2
		self.vetor3 = vetor3

	def getBase(self):
		return self.vetor1.getVetor(), self.vetor2.getVetor(), self.vetor3.getVetor()  
  
#FUNÇÕES
def produtoEscalar(vetor1, vetor2):
    produto1 = vetor1.x * vetor2.x
    produto2 = vetor1.y * vetor2.y
    produto3 = vetor1.z * vetor2.z
    soma = produto1 + produto2 + produto3
    return soma

def norma(vetor):
    return math.sqrt(produtoEscalar(vetor, vetor))

def normalize(vetor):
    normaVetor = norma(vetor)
    x = vetor.x / normaVetor
    y = vetor.y / normaVetor
    z = vetor.z / normaVetor 
    vetorNormalidado = Vetor(x, y, z)
    return vetorNormalidado  
  
def cosseno(vetor1, vetor2):
  prodEscalar = produtoEscalar(vetor1, vetor2)
  normaV1 = norma(vetor1)
  normaV2 = norma(vetor2)
  cosseno = (prodEscalar)/(normaV1*normaV2)
  return cosseno

def projecao(vetor, arg):
    if isinstance(arg, Vetor):
      vetor1 = vetor
      vetor2 = arg
      prodEscalar = produtoEscalar(vetor1, vetor2)
      vetorModuloQuadrado = math.pow(norma(vetor2), 2)
      mt = prodEscalar / vetorModuloQuadrado
      resp = Vetor(vetor2.x*mt, vetor2.y*mt,vetor2.z*mt)
      return resp
    
    elif isinstance(arg, Reta):
      reta = arg
      vetorDiretor = diretor(reta)
      produtoEscalar1 = produtoEscalar(vetor, vetorDiretor)
      normaVetorDiretor = norma(vetorDiretor)
      divisaoProdutoNorma = produtoEscalar1 / (normaVetorDiretor**2)
      x = vetorDiretor.x * divisaoProdutoNorma
      y = vetorDiretor.y * divisaoProdutoNorma
      z = vetorDiretor.z * divisaoProdutoNorma
      return Vetor(x, y, z)

def produtoVetorial(vetor1: Vetor, vetor2: Vetor):
    x = (vetor1.getY() * vetor2.getZ()) - (vetor1.getZ() * vetor2.getY())
    y = (vetor1.getZ() * vetor2.getX()) - (vetor1.getX() * vetor2.getZ())
    z = (vetor1.getX() * vetor2.getY()) - (vetor1.getY() * vetor2.getX())
    return Vetor(x, y, z)

def reflexao(vetor1, vetor2):
    proj12 = projecao(vetor1, vetor2)
    vetor3 = Vetor(vetor1.x - 2*proj12.x, vetor1.y - 2*proj12.y, vetor1.z - 2*proj12.z)
    return vetor3

def saoParalelos(vetor1, vetor2):
	div1 = 0
	div2 = 0
	div3 = 0

	if vetor1.x*vetor2.x != 0:
		div1 = vetor1.x/vetor2.x
	if vetor1.y*vetor2.y != 0:
		div2 = vetor1.y/vetor2.y
	if vetor1.z*vetor2.z != 0:
		div3 = vetor1.z/vetor2.z

	if ((div1 != 0) and (div1 == div2 and div2 == div3)):
		return True
	elif ((vetor1.x == 0 and vetor1.y == 0 and vetor1.z == 0) or (vetor2.x == 0 and vetor2.y == 0 and vetor2.z == 0)): 
		return True
	else: 
		return False 

def saoOrtogonais(vetor1, vetor2):
  prodEscalar = produtoEscalar(vetor1, vetor2)
  # Sao ortogonais quando o produto escalar e igual a zero
  if prodEscalar == 0:
    return True
  else:
    return False

def eLI(vetores):

    if(len(vetores) == 2):
        paralelismo = saoParalelos(arrayVetores[0], arrayVetores[1])
    else:
        paralelismo = saoParalelos(arrayVetores[0], arrayVetores[1]) or saoParalelos(arrayVetores[0], arrayVetores[2]) or saoParalelos(arrayVetores[1], arrayVetores[2])

      #false se tem paralelismo  
    return not paralelismo

def projecaoPlano(vetor, plano):

  mult = produtoEscalar(vetor, plano.getVetorNormal()) / produtoEscalar(plano.getVetorNormal(), plano.getVetorNormal())

  x = vetor.getX() - (mult * plano.vetorNormal.getX())
  y = vetor.getY() - (mult * plano.vetorNormal.getY())
  z = vetor.getZ()- (mult * plano.vetorNormal.getZ())
  
  vetorProj = Vetor(x, y, z)
  
  return vetorProj.getVetor()

def formaCartesianaReta(reta):
    a = reta.vetordiretor.getY()/reta.vetordiretor.getX()
    b = -1
    c = 0
    d = reta.ponto.getY() - (a * reta.ponto.getX())
    e = 0
    f = reta.vetordiretor.getZ()/reta.vetordiretor.getY()
    g = -1
    h = reta.ponto.getZ() - (e * reta.ponto.getY())
    
    return [[a, b, c, d], [e, f, g, h]]


##OBJETOS

def diretor(reta):
    return reta.vetordiretor
  
def normal(plano: Plano):
  # Nao sei se é assim, ta parecendo muito simples
  resp = plano.vetorNormal
  return resp

def eParalelo(vetor, reta):
	x = ((vetor.y * reta.vetordiretor.getZ()) - (vetor.z * reta.vetordiretor.getY()))
	y = ((vetor.z * reta.vetordiretor.getX()) - (vetor.x * reta.vetordiretor.getZ()))
	z = ((vetor.x * reta.vetordiretor.getY()) - (vetor.y * reta.vetordiretor.getX()))
	if (x == 0 and y == 0 and z == 0):
		return True
	else :
		return False

def eOrtogonal(vetor, plano):
  return saoParalelos(vetor, plano.vetorNormal)

def componenteOrtogonal(vetor, plano):
  # Nao sei se é assim, ta parecendo muito simples 2
  # Projecao do vetor no vetor ortogonal do plano
  vetorOrtogonal = normal(plano) 
  componente = projecao(vetor, vetorOrtogonal)
  return componente

def saoComplementosOrtogonais(reta, plano):
	x1 = plano.vetorNormal.getX()
	y1 = plano.vetorNormal.getY()
	z1 = plano.vetorNormal.getZ()

	x2 = reta.vetordiretor.getX()
	y2 = reta.vetordiretor.getY()
	z2 = reta.vetordiretor.getZ()

	vetorP = Vetor(x1, y1, z1)
	vetorR = Vetor(x2, y2, z2)

	if (saoParalelos(vetorP, vetorR)):
		return True
	else:
		return False

def saoComplementosOrtogonais2(plano, reta):
  return eOrtogonal(reta.vetordiretor, plano)

def formaCartesiana(plano):
  produto1 = plano.vetorNormal.getX() * plano.ponto.getX()
  produto2 = plano.vetorNormal.getY() * plano.ponto.getY()
  produto3 = plano.vetorNormal.getZ() * plano.ponto.getZ()
  constante = - produto1 - produto2 - produto3
  return [plano.vetorNormal.getX(), plano.vetorNormal.getY(), plano.vetorNormal.getZ(), constante]




#INTERSECOES

def intersecao(reta1, reta2): # Falta testar, pois falta a função formaCartesiana(reta)
  #Verifica se tem interseção:
  formaCartesiana2 = formaCartesiana(reta2)
  
  v1 = Vetor(reta1.ponto.x, reta1.ponto.y, reta1.ponto.z)
  v2 = Vetor(formaCartesiana2[0][0], formaCartesiana2[0][1], formaCartesiana2[0][2])
  v3 = Vetor(formaCartesiana2[1][0], formaCartesiana2[1][1], formaCartesiana2[1][2])

  produto1 = produtoEscalar(v1, v2) #(p, q, r)*(a, b, c)
  produto2 = produtoEscalar(v1, v3) #(p, q, r)*(e, f, g)
  produto3 = produtoEscalar(reta1.vetordiretor, v2) #(x, y, z)*(a, b, c)
  produto4 = produtoEscalar(reta1.vetordiretor, v3) #(x, y, z)*(e, f, g)

  t1 = (produto1 + formaCartesiana[0][3]) / produto3
  t2 = (produto2 + formaCartesiana[1][3]) / produto4

  if t1 == t2: #Se t1 == t2, então existe interseção
    if eParalelo(reta1.vetordiretor, reta2):
      return vetor1
    else:
      x = reta1.ponto.x + (reta1.vetordiretor.x * t1)
      y = reta1.ponto.y + (reta1.vetordiretor.y * t1)
      z = reta1.ponto.z + (reta1.vetordiretor.z * t1)
      return Ponto(x, y, z)
  else:
    return None

def intersecao2(reta, plano):
  a = plano.vetorNormal.x
  b = plano.vetorNormal.y
  c = plano.vetorNormal.z
  d = -1 * produtoEscalar(plano.vetorNormal, Vetor(plano.ponto.x, plano.ponto.y, plano.ponto.z))

  if(produtoEscalar(reta.vetordiretor, plano.vetorNormal) == 0):
    if(a*reta.ponto.x + b*reta.ponto.y + c*reta.ponto.z + d == 0):
      return reta
    else:
      return None

  t = (-1 * (a*reta.ponto.x + b*reta.ponto.y + c*reta.ponto.z + d)) / (a*reta.vetordiretor.x + b*reta.vetordiretor.y + c*reta.vetordiretor.z)

  return Ponto(reta.ponto.x + t*reta.vetordiretor.x, reta.ponto.y + t*reta.vetordiretor.y, reta.ponto.z + t*reta.vetordiretor.z)

def intersecao(reta, esfera):
	xC = esfera.ponto.getX() - reta.ponto.getX()
	yC = esfera.ponto.getY() - reta.ponto.getY()
	zC = esfera.ponto.getZ() - reta.ponto.getZ()

	vetorCentro = Vetor(xC, yC, zC)
	Proj = projecao(vetorCentro, reta)
	ModulovC = norma(vetorCentro)
	ModuloProj = norma(Proj)

	D = ((ModulovC ** 2) - (ModuloProj ** 2) ** (1/2))

	r = esfera.getRaio()

	if (D > r):
		return "Não há intersecao"
	elif (D == r) :
		# aT2 + bT + c
		A = produtoEscalar(reta.vetordiretor, reta.vetordiretor) #Produto Escalar entre os vetores diretores da reta
		b0 = produtoEscalar(reta.vetordiretor, vetorCentro) #2 vezes o produto escalar de Vd e PC
		B = b0*2
		c0 = produtoEscalar(vetorCentro, vetorCentro) # Produto escalar de PC com PC menos o quadrado do raio
		C = c0 - (esfera.getRaio()**2)

		T1 = (-B/(2*A)) # Só haverá um valor para T, já que o delta será igual a ZERO

		X = reta.ponto.getX() - (T1 * reta.vetordiretor.getX())
		Y = reta.ponto.getY() - (T1 * reta.vetordiretor.getY())
		Z = reta.ponto.getZ() - (T1 * reta.vetordiretor.getZ())

		return (X, Y, Z)
	else :
		A = produtoEscalar(reta.vetordiretor, reta.vetordiretor)
		b0 = produtoEscalar(reta.vetordiretor, vetorCentro)
		B = b0*2
		c0 = produtoEscalar(vetorCentro, vetorCentro)
		C = c0 - (esfera.getRaio()**2)

		Delta = ((B**2) - (4*A*C))

		T1 = (-B + (Delta**(1/2)))/(2*A)
		T2 = (-B - (Delta**(1/2)))/(2*A)

		X1 = reta.ponto.getX() - (T1 * reta.vetordiretor.getX())
		Y1 = reta.ponto.getY() - (T1 * reta.vetordiretor.getY())
		Z1 = reta.ponto.getZ() - (T1 * reta.vetordiretor.getZ())

		X2 = reta.ponto.getX() - (T2 * reta.vetordiretor.getX())
		Y2 = reta.ponto.getY() - (T2 * reta.vetordiretor.getY())
		Z2 = reta.ponto.getZ() - (T2 * reta.vetordiretor.getZ())

		return ((X1, Y1, Z1) , (X2, Y2, Z2))


#BASE

def ortogonalize(base: Base):
  v1 : Vetor = base.vetor1
  v2 : Vetor = base.vetor2
  v3 : Vetor = base.vetor3

  vAux = Vetor(0, 0, 0)

  vProj = projecao(v2, v1)
  v2.x = v2.x - vProj.x
  v2.y = v2.y - vProj.y
  v2.z = v2.z - vProj.z

  vAux = v3
  vProj = projecao(vAux, v1)
  v3.x = v3.x - vProj.x
  v3.y = v3.y - vProj.y
  v3.z = v3.z - vProj.z
  vProj = projecao(vAux, v2)
  v3.x = vAux.x - vProj.x
  v3.y = vAux.y - vProj.y
  v3.z = vAux.z - vProj.z

  return Base(v1, v2, v3)


def mudeBase(vetor, base):
  #return (Vetor(vetor.x * base.vetor1.x + vetor.y * base.vetor2.x + vetor.z * base.vetor3.x, vetor.x * base.vetor1.y + vetor.y * base.vetor2.y + vetor.z * base.vetor3.y, vetor.x * base.vetor1.z + vetor.y * base.vetor2.z + vetor.z * base.vetor3.z))
  v1 = Vetor(base.vetor1.x, base.vetor1.y, base.vetor1.z)
  v2 = Vetor(base.vetor2.x, base.vetor2.y, base.vetor2.z)
  v3 = Vetor(base.vetor3.x, base.vetor3.y, base.vetor3.z)
  v4 = vetor

  if(v1.x == 0):
    ax1 = v1.x 
    ax2 = v2.x 
    ax3 = v3.x 
    ax4 = v4.x 
    if(v1.y != 0):
      v1.x = v1.y
      v2.x = v2.y
      v3.x = v3.y
      v4.x = v4.y

      v1.y = ax1 
      v2.y = ax2 
      v3.y = ax3 
      v4.y = ax4 
    elif(v1.z != 0):
      v1.x = v1.z 
      v2.x = v2.z 
      v3.x = v3.z
      v4.x = v4.z 

      v1.z = ax1 
      v2.z = ax2 
      v3.z = ax3 
      v4.z = ax4 

  c = v1.y/v1.x
  v1.y = v1.y - v1.x*c 
  v2.y = v2.y - v2.x*c 
  v3.y = v3.y - v3.x*c 
  v4.y = v4.y - v4.x*c

  c = v1.z/v1.x
  v1.z = v1.z - v1.x*c 
  v2.z = v2.z - v2.x*c 
  v3.z = v3.z - v3.x*c 
  v4.z = v4.z - v4.x*c

  if(v2.y == 0):
    ay2 = v2.y 
    ay3 = v3.y 
    ay4 = v4.y 

    v2.y = v2.z 
    v3.y = v3.z 
    v4.y = v4.z 

    v2.z = ay2 
    v3.z = ay3 
    v4.z = ay4

  c = v2.z/v2.y 
  v2.z = v2.z - v2.y*c 
  v3.z = v3.z - v3.y*c
  v4.z = v4.z - v4.y*c

  c = v4.z/v3.z 
  b = (v4.y - v3.y*c)/v2.y 
  a = (v4.x - v3.x*c - v2.x*b)

  return Vetor(a, b, c)
  return [[v1.x, v1.y, v1.z], [v2.x, v2.y, v2.z], [v3.x, v3.y, v3.z]]

#TRANSFORMACOES LINEARES

def reflexao3(vetor, vetorDiretor):
  return reflexao(vetor, vetorDiretor)

def reflexao4(vetor: Vetor):
  # Matriz de reflexão em relação a origem:
  # -1  0  0
  #  0 -1  0
  #  0  0 -1
  return Vetor(vetor.x * (-1), vetor.y * (-1), vetor.z * (-1))


def rotacao(vetor: Vetor, angulo, sentido, reta: Reta):
  # Ideia: Combinar uma mudanca de base com rotacao notoria
  v: Vetor = reta.vetordiretor

  # nova base orgonormal: precisa de uma nova base com v1, v2 e v3 (tres novos vetores)
  #v1
  v1: Vetor = normalize(v) #(v/norma(v))

  #v2
  if v1.getY() == 0:
    v2aux = Vetor(0, 1, 0)
  else:
    v2aux = Vetor(0, 1, ((-1*v1.getY())/v1.getZ()))

  v2: Vetor = normalize(v2aux) #(v2aux/norma(v2aux))

  #v3
  v3aux = produtoVetorial(v1, v2)
  v3: Vetor = normalize(v3aux) #(v3aux/norma(v3aux))

  # rotacoes: tres operacoes rt1, rt2, rt3 feitas atraves de matrizes
  # operacao 1: 
  novaBase = Base(v1, v2, v3)
  rt1: Vetor = mudeBase(vetor, novaBase)

  # operacao 2: rotacao notoria usando a base nova criada; rotacao no eixo X
  # rt2 = rotação(rt1, angulo, sentido)
  if sentido == 'AH':
    xRt2 = rt1.getX()
    yRt2 = rt1.getY()*math.cos(angulo)-rt1.getZ()*math.sin(angulo)
    zRt2 = rt1.getY()*math.sin(angulo)+rt1.getZ()*math.cos(angulo)
    rt2 = Vetor(xRt2, yRt2, zRt2)
  elif sentido == 'H':
    xRt2 = rt1.getX()
    yRt2 = rt1.getY()*math.cos(angulo)+rt1.getZ()*math.sin(angulo)
    zRt2 = ((-1)*(rt1.getY()*math.sin(angulo)))+rt1.getZ()*math.cos(angulo)
    rt2 = Vetor(xRt2, yRt2, zRt2)

  # operacao 3: multiplicacao de matriz do vetor rt2 com a matriz formada pelos vetores da novaBase
  xRt3 = v1.getX()*rt2.getX() + v2.getX()*rt2.getY() + v3.getX()*rt2.getZ()
  yRt3 = v1.getY()*rt2.getX() + v2.getY()*rt2.getY() + v3.getY()*rt2.getZ()
  zRt3 = v1.getZ()*rt2.getX() + v2.getZ()*rt2.getY() + v3.getZ()*rt2.getZ()
  rt3 = Vetor(xRt3, yRt3, zRt3)

  return rt3


def cisalhamento(vetor: Vetor, eixos, fator1, fator2):
  # Fiquei bem confuso com a explicacao de Lucio, mas creio eu que seja assim.
  # Se tiver algo de errado, so falar :)
  x0 = vetor.getX()
  y0 = vetor.getY()
  z0 = vetor.getZ()
  a = fator1
  b = fator2

  if eixos == 'XYZ':
    resp = Vetor((x0 + a*y0 + b*z0), y0, z0)
  elif eixos == 'YZX':
    # Fiquei confuso porque a especificacao colocou YZX.
    # Caso seja YXZ a resposta seria resp = Vetor(x0, (y0 + a*x0 + b*z0), z0)
    resp = Vetor(x0, (y0 + a*z0 + b*x0), z0)
  elif eixos == 'ZXY':
    resp = Vetor(x0, y0, (z0 + a*x0 + b*y0))

  return resp


#TESTES
vetor1 = Vetor(2, 1, -2)
vetor2 = Vetor(4, 4, 2)
vetor3 = Vetor(2, 3, 4)
vetor4 = Vetor(1, -1, 0)
esfera = Esfera(Ponto(2, 1, -2), 6)
print(vetor1.getVetor())

print(produtoEscalar(vetor1, vetor2)) #ProdutoEscalar
vv = projecao(vetor3,vetor4)
print(vv.x, vv.y, vv.z) #Projeção
rr = reflexao(vetor1, vetor2)
print(rr.x, rr.y, rr.z)
print(esfera.getCentro(), esfera.getRaio())
print(norma(vetor1), norma(rr))

ponto = Ponto(2, -1, 3)
vetorNormal = Vetor(3, 2, -4)
plano = Plano(ponto, vetorNormal)
print(formaCartesiana(plano))

vetor5 = Vetor(1, 1, 1)
vetor6 = Vetor(-1, 0, 1)
print(saoOrtogonais(vetor5, vetor6)) #SaoOrgotonais
print(cosseno(vetor5, vetor6)) #Cosseno

reta = Reta(Ponto(1, 2, 3), Vetor(4, 2, 2))
p = projecao(Vetor(1, 2, 3), reta) #Projeção vetor na reta
print(p.getVetor())

print(normal(plano).getVetor()) #Normal do Plano
print(componenteOrtogonal(vetor5, plano).getVetor()) #Componente Orgotogal
print(projecaoPlano(vetor5, plano))
print(formaCartesianaReta(reta))
print(cisalhamento(vetor5, 'XYZ', 1, 1).getVetor()) #Cisalhamento 2 fatores
print(rotacao(vetor5, math.radians(180), 'H', reta).getVetor()) #Rotacao arbitraria

base1 = Base(Vetor(0, 0, 1), Vetor(0, 1, 1), Vetor(1, 1, 1))
print(ortogonalize(base1).getBase())
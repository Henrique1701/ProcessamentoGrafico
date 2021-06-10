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
    vetorNormalidado = [x, y, z]
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

def componenteOrtogonal(vetor, plano):
  # Nao sei se é assim, ta parecendo muito simples 2
  # Projecao do vetor no vetor ortogonal do plano
  vetorOrtogonal = normal(plano) 
  componente = projecao(vetor, vetorOrtogonal)
  return componente

def saoComplementosOrtogonais(plano, reta):
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

def formaCartesiana(plano):
  produto1 = plano.vetorNormal.getX() * plano.ponto.getX()
  produto2 = plano.vetorNormal.getY() * plano.ponto.getY()
  produto3 = plano.vetorNormal.getZ() * plano.ponto.getZ()
  constante = - produto1 - produto2 - produto3
  return [plano.vetorNormal.getX(), plano.vetorNormal.getY(), plano.vetorNormal.getZ(), constante]

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
print(componenteOrtogonal(vetor5, plano).getVetor()) #ComponenteOrtogonal

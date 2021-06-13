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

#BASE

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

  return [a, b, c]
  return [[v1.x, v1.y, v1.z], [v2.x, v2.y, v2.z], [v3.x, v3.y, v3.z]]

#TRANSFORMACOES LINEARES

def reflexao3(vetor, vetorDiretor):
  return reflexao(vetor, vetorDiretor)

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
print(componenteOrtogonal(vetor5, plano).getVetor()) #
print(projecaoPlano(vetor5, plano))
print(formaCartesianaReta(reta))

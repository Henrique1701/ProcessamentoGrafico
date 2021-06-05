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

class Reta:
    def __init__(self, ponto, vetordiretor):
        self.ponto = ponto
        self.vetordiretor = vetordiretor
  
class Esfera:
  def __init__(self, ponto, raio):
      self.ponto = ponto #Usei o Ponto pra fazer o centro porque é mesma estrutura
      self.raio = raio 

  def getEsfera(self):
    return self.ponto.getPonto(), self.raio
  def getCentro(self):
    return self.ponto.getPonto()
  def getRaio(self):
    return self.raio

#FUNÇÕES
def produtoEscalar(vetor1, vetor2):
    produto1 = vetor1.x * vetor2.x
    produto2 = vetor1.y * vetor2.y
    produto3 = vetor1.z * vetor2.z
    soma = produto1 + produto2 + produto3
    return soma

def norma(vetor):
    return math.sqrt(produtoEscalar(vetor, vetor))

def projecao(vetor1, vetor2):
    prodEscalar = produtoEscalar(vetor1, vetor2)
    vetorModuloQuadrado = vetor2.x**2 + vetor2.y**2 + vetor2.z**2 #checar o modulo(abs) dessa parte depois q nao tava indo
    proj = prodEscalar / vetorModuloQuadrado
    resp = Vetor(vetor2.x*proj, vetor2.y*proj,vetor2.z*proj)
    return resp.getVetor()


#TESTES
vetor1 = Vetor(2, 1, -2)
vetor2 = Vetor(4, 4, 2)
esfera = Esfera(Ponto(2, 1, -2), 6)
print(vetor1.getVetor())

print(produtoEscalar(vetor1, vetor2)) #ProdutoEscalar
print(projecao(vetor1,vetor2)) #Projeção
print(esfera.getCentro(), esfera.getRaio())
print(norma(vetor1))

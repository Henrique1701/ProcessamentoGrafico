from math import sqrt

def Vetor(x1, x2, x3):
    return [x1, x2, x3]

def produtoEscalar(vetor1, vetor2):
    produto1 = vetor1[0] * vetor2[0]
    produto2 = vetor1[1] * vetor2[1]
    produto3 = vetor1[2] * vetor2[2]
    soma = produto1 + produto2 + produto3
    return soma

def norma(vetor):
    resultadoParcial = (vetor[0]**2) + (vetor[1]**2) + (vetor[2]**2)
    resultado = sqrt(resultadoParcial)
    return resultado

def normalize(vetor):
    normaVetor = norma(vetor)
    x = vetor[0] / normaVetor
    y = vetor[1] / normaVetor
    z = vetor[2] / normaVetor 
    vetorNormalidado = [x, y, z]
    return vetorNormalidado

def cosseno(vetor1, vetor2):
    prodEscalarVetor12 = produtoEscalar(vetor1, vetor2)
    normaVetor1 = norma(vetor1)
    normaVetor2 = norma(vetor2)
    cos = prodEscalarVetor12 / (normaVetor1 * normaVetor2)
    return cos #Verificar se esse resultado já está em radianos
    

# Testes:
vetor1 = Vetor(2, 1, -2)
vetor2 = Vetor(4, 4, 2)

produtoVetor12 = produtoEscalar(vetor1, vetor2)

normaVetor1 = norma(vetor1)

normalizeVetor1 = normalize(vetor1)
normaTeste = norma(normalizeVetor1)

print(normalizeVetor1)
print(normaTeste)

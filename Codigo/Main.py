import math
import time
import matplotlib.pyplot as plt
import helpers
from functools import reduce


def tpotencia(x, y, z):
    yp = [math.log(itens) for itens in y]
    xy = [iten1*iten2 for iten1, iten2 in zip(x, yp)]
    xquad = [itens**2 for itens in x]
    somax = reduce(lambda x, y: x+y, x)
    somaxy = reduce(lambda x, y: x+y, xy)
    somaxquad = reduce(lambda x, y: x+y, xquad)
    somayp = reduce(lambda x, y: x+y, yp)
    b = math.exp(helpers.Descobre_A(len(x), somax, somayp, somaxy, somaxquad))
    a = math.exp(helpers.Descobre_B(len(x), somax, somayp, somaxy, somaxquad))
    retorn = helpers.FuncPotencia(len(x), x, a, b)
    ideal = helpers.VerificaViabilidade(len(x), y, retorn)
    if str(z).lower() == 'b':
        helpers.tabPotencia(x, yp, xy, xquad, somax, somayp, somaxy, somaxquad, a, b, ideal, retorn)
        helpers.plotCurva(x, y, retorn, "Potencia")
    return retorn



def thiperbolica(x, y, z):
    yhip = [(1/itens) for itens in y]
    xy = [iten1*iten2 for iten1, iten2 in zip(x, yhip)]
    xquad = [itens**2 for itens in x]
    somax = reduce(lambda x, y: x+y, x)
    somaxy = reduce(lambda x, y: x+y, xy)
    somaxquad = reduce(lambda x, y: x+y, xquad)
    somayhip = reduce(lambda x, y: x+y, yhip)
    a = helpers.Descobre_A(len(x), somax, somayhip, somaxy, somaxquad)
    b = helpers.Descobre_B(len(x), somax, somayhip, somaxy, somaxquad)
    retorna = helpers.FuncHiperbolica(len(x), x, a, b)
    ide = helpers.VerificaViabilidade(len(x), y, retorna)
    if str(z).lower() == 'a':
        helpers.tabHiperbolica(x, yhip, xy, xquad, somax, somayhip, somaxy, somaxquad, a, b, ide, retorna)
        helpers.plotCurva(x, y, retorna, "HIPERBOLICA")
    return retorna

    
def texponencial(x, y, z):
    yexp = [math.log(itens) for itens in y]
    xy = [iten1*iten2 for iten1,iten2 in zip(x, yexp)]
    xquad = [iten**2 for iten in x]
    somax = reduce(lambda x, y: x+y, x)
    somaxy = reduce(lambda x, y: x+y, xy)
    somaxquad = reduce(lambda x, y: x+y, xquad)
    somayexp = reduce(lambda x, y: x+y, yexp)
    a = helpers.Descobre_A(len(x), somax, somayexp, somaxy, somaxquad)
    b = helpers.Descobre_B(len(x), somax, somayexp, somaxy, somaxquad)
    retorno = helpers.funcExponencial(len(x), x, a, math.exp(b))
    ide = helpers.VerificaViabilidade(len(x), y, retorno)
    if str(z).lower() == 'c':
        helpers.tabExpo(x, yexp, xy, xquad, somax, somayexp, somaxy, somaxquad, a, b, ide, retorno)
        helpers.plotCurva(x, y, retorno, "EXPONENCIAL")
    return retorno
    
    
    

def tgeometrica(x, y, z):
    xge = [math.log(iten) for iten in x]
    yge = [math.log(iten) for iten in y]
    xy = [iten1 * iten2 for iten1, iten2 in zip(xge, yge)]
    xquad = [itens **2 for itens in x]   
    somax = reduce(lambda x, y: x+y, xge)
    somaxy = reduce(lambda x, y: x+y, xy)
    somaxquad = reduce(lambda x, y: x+y, xquad)
    somayge = reduce(lambda x, y: x+y, yge)
    b = helpers.Descobre_A(len(x), somax, somayge, somaxy, somaxquad)
    a = math.log(helpers.Descobre_B(len(x), somax, somayge, somaxy, somaxquad))
    x = list(map(math.log, x))
    ret = helpers.funcGeometrica(len(x), x, a, b)
    ide = helpers.VerificaViabilidade(len(x), y, ret)
    if str(z).lower() == 'd':
        helpers.tabGeo(a, b, x, yge, xy, xquad, somax, somayge, somaxy, somaxquad, ide)
        helpers.plotCurva(x, y, ret, "GEOMÉTRICA")
    return ret


if __name__ == "__main__":
    
    x = []
    y = []
    escolha = 0
    potencia, hiperbole = 0, 0
    i = 0
    restraingeometric = False
    print("Quantos pontos você quer inserir para o ajuste")
    c = int(input())
    print("insira os valores de x\n")
    for i in range(c):
        x.append(float(input()))
    print("insira os valores de y\n")
    for i in range(c):
        y.append(float(input()))
    while True:
        print("Qual aproximação você acha a mais adequada?")
        print("[A] Hiperbólica\n[B] Curva Exponencial\n[C] Exponencial\n[D] Geométrica\n[E] comparativo")
        z = input()
        if z == 'a' or z == 'A':

            thiperbolica(x, y, z)
        elif z == 'b' or z == 'B':
            tpotencia(x, y, z)
        elif z == 'c' or z == 'C':
            texponencial(x, y, z)
        elif z == 'd' or z == 'D':
            tgeometrica(x, y, z)
        elif z == 'e' or z == 'E':
            geometria = tgeometrica(x, y, z)
            variancia1, variancia2, i = 0, 0, 0
            potencia = tpotencia(x, y, z)
            exponencial = texponencial(x, y, z)
            hiperbole = thiperbolica(x, y, z)
            plt.plot(x, y, label='Ideal')
            plt.plot(x, hiperbole, label='Curva Hiperbole')
            plt.plot(x, potencia, label='Curva Potencia')
            plt.plot(x, exponencial, label='Curva Exponencial')
            plt.plot(x, geometria, label='Curva Geométrica')
            plt.legend()
            time.sleep(15)
            plt.show()
        else:
            break

        break

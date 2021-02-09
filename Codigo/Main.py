import math
import time

import matplotlib.pyplot as plt


def VerificaViabilidade(tamanho, refy, real):
    fx, hx = refy, real
    decreta, i, soma = 0, 0, 0
    for i in range(tamanho):
        soma += ((fx[i] - hx[i]) ** 2)
    decreta = (soma ** (1 / 2))
    return decreta


def funcExponencial(n, referenciax, referenciay, a, b, z):
    y, exp = 0, []
    for y in range(n):
        resultado = (b * math.exp(a * referenciax[y]))
        exp.append(resultado)
    return exp


def FuncHiperbolica(n, referenciax, referenciay, a, b, z):
    y = 0
    hip = []
    for y in range(n):
        resultado = (1 / (a * referenciax[y] + b))
        hip.append(resultado)
    return hip


def FuncPotencia(n, referenciax, referenciay, a, b, z):
    l = 0
    pot = []
    for l in range(0, n):
        resultant = (a * (b ** referenciax[l]))
        pot.append(resultant)

    return pot


def funcGeometrica(n, referenciax, referenciay, a, b, z):
    l = 0
    geo = []
    for l in range(0, n):
        resultant = (a * (referenciax[l] ** b))
        geo.append(resultant)

    return geo


def Descobre_B(n, somax, somay, somaxy, somax2):
    xy, y, x2, x = somaxy, somay, somax2, somax
    resultado2 = (((x * xy) - (y * x2)) / ((x ** 2) - (n * x2)))
    return resultado2


def Descobre_A(n, somax, somay, somaxy, somax2):
    xy, y, x2, x = somaxy, somay, somax2, somax
    resultado = (((n * xy) - (x * y)) / ((n * x2) - (x ** 2)))
    return resultado


def TabPotencia(x, y, z):
    i, j, a, b, acerto, bcerto, inverte, ideal = 0, 0, 0, 0, 0, 0, 0, 0
    bora = z
    yp, xy, xquad, = [], [], []
    somax, somaxy, somayp, somaxquad = 0, 0, 0, 0
    for i in range(len(x)):
        yp.append(math.log(y[i]))
        xy.append(x[i] * yp[i])
        xquad.append(x[i] ** 2)
    for j in range(len(x)):
        somax += x[j]
        somaxy += xy[j]
        somaxquad += xquad[j]
        somayp += yp[j]
    a = Descobre_A(len(x), somax, somayp, somaxy, somaxquad)
    b = Descobre_B(len(x), somax, somayp, somaxy, somaxquad)
    inverte = a
    a = b
    b = inverte
    acerto = math.exp(a)
    bcerto = math.exp(b)
    retorn = FuncPotencia(len(x), x, y, acerto, bcerto, bora)
    ideal = VerificaViabilidade(len(x), y, retorn)
    if z == 'b' or z == 'B':
        print("TABELA DA CURVA AB^x")
        for j in range(len(x)):
            if x[j] >= 0:
                print(f' {x[j]:.3f} | {yp[j]:.3f} | {xy[j]:.3f}  | {xquad[j]:.3f}')
            else:
                print(f'{x[j]:.3f} | {yp[j]:.3f} | {xy[j]:.3f} | {xquad[j]:.3f}')
        if somax >= 0:
            print(f'  {somax:.3f} | {somayp:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        else:
            print(f' {somax:.3f} | {somayp:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        print('\n')
        print(f'a ={acerto} e b = {bcerto}, o que forma a seguinte função: ', end='')
        print(f'\n {acerto} * {bcerto}^x\n\n')
        print("o erro quadratico é de {}".format(ideal))
        fig, ax = plt.subplots()
        plt.plot(x, y, label='Ideal')
        plt.plot(x, retorn, label='Curva Potencia')
        ax.legend()
        time.sleep(15)
        plt.show()
    return retorn


def TabHiperbolica(x, y, z):
    func, retorna, ide, i, j, a, b, somax, somaxy, somayhip, somaxquad = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    parametro = z
    yhip, xy, xquad = [], [], []
    for i in range(len(x)):
        yhip.append(1 / y[i])
        xy.append(x[i] * yhip[i])
        xquad.append(x[i] ** 2)
    for j in range(len(x)):
        somax += x[j]
        somayhip += yhip[j]
        somaxy += xy[j]
        somaxquad += xquad[j]

    a = Descobre_A(len(x), somax, somayhip, somaxy, somaxquad)
    b = Descobre_B(len(x), somax, somayhip, somaxy, somaxquad)
    retorna = FuncHiperbolica(len(x), x, y, a, b, parametro)
    ide = VerificaViabilidade(len(x), y, retorna)
    if z == 'a' or z == 'A':
        print("TABELA DA FUNÇÃO HIPERBOLICA")
        for j in range(len(x)):
            if x[j] >= 0:
                print(f'  {x[j]:.3f} | {yhip[j]:.3f} | {xy[j]:.3f}  | {xquad[j]:.3f}')
            else:
                print(f' {x[j]:.3f} | {yhip[j]:.3f} | {xy[j]:.3f} | {xquad[j]:.3f}')
        if somax >= 0:
            print(f'  {somax:.3f} | {somayhip:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        else:
            print(f' {somax:.3f} | {somayhip:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        print('\n')
        print(f'a ={a} e b = {b}, o que forma a seguinte função: ', end='')
        print(f' 1/{a} * x +{b}\n\n')
        print("o erro quadratico é de {} ".format(ide))
        print("e este é o gráfico: ")
        fig, ax = plt.subplots()
        plt.plot(x, y, label='Ideal')
        plt.plot(x, retorna, label='Curva Hiperbole')
        ax.legend()
        time.sleep(10)
        plt.show()
    return retorna


def tabExponencial(x, y, z):
    func, retina, ide, i, j, a, b, somax, somaxy, somayexp, somaxquad = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    parametro = z
    yexp, xy, xquad = [], [], []
    for i in range(len(x)):
        yexp.append(math.log(y[i]))
        xy.append(x[i] * yexp[i])
        xquad.append(x[i] ** 2)
    for j in range(len(x)):
        somax += x[j]
        somayexp += yexp[j]
        somaxy += xy[j]
        somaxquad += xquad[j]

    a = Descobre_A(len(x), somax, somayexp, somaxy, somaxquad)
    b = Descobre_B(len(x), somax, somayexp, somaxy, somaxquad)
    retina = funcExponencial(len(x), x, y, a, math.exp(b), parametro)
    ide = VerificaViabilidade(len(x), y, retina)
    if z == 'c' or z == 'C':
        print("TABELA DA FUNÇÃO EXPONENCIAL")
        for j in range(len(x)):
            if x[j] >= 0:
                print(f'  {x[j]:.3f} | {yexp[j]:.3f} | {xy[j]:.3f}  | {xquad[j]:.3f}')
            else:
                print(f' {x[j]:.3f} | {yexp[j]:.3f} | {xy[j]:.3f} | {xquad[j]:.3f}')
        if somax >= 0:
            print("Somatoria dos valores")
            print(f' x = {somax:.3f} |y = {somayexp:.3f} | x*y = {somaxy:.3f}  | x^2 = {somaxquad:.3f}')
        else:
            print(f' {somax:.3f} | {somayexp:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        print('\n')
        print(f'a ={a} e b = {math.exp(b)}, o que forma a seguinte função: ', end='')
        print(f' {math.exp(b)} * e^({a}*x)\n\n')
        print("o erro quadratico é de {} ".format(ide))
        print("e este é o gráfico: ")
        fig, ax = plt.subplots()
        plt.plot(x, y, label='Ideal')
        plt.plot(x, retina, label='Curva Exponencial')
        ax.legend()
        time.sleep(10)
        plt.show()

    return retina


def tabGeometrica(x, y, z):
    func, ret, ide, i, j, a, b, somax, somaxy, somayge, somaxquad = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    parametro, inverte = z, 0
    xge, yge, xy, xquad = [], [], [], []
    for i in range(len(x)):
        xge.append(math.log(x[i]))
        yge.append(math.log(y[i]))
        xy.append(x[i] * y[i])
        xquad.append(x[i] ** 2)
    for j in range(len(x)):
        somax += xge[j]
        somayge += y[j]
        somaxy += xy[j]
        somaxquad += xquad[j]

    a = Descobre_A(len(x), somax, somayge, somaxy, somaxquad)
    b = Descobre_B(len(x), somax, somayge, somaxy, somaxquad)
    inverte = a
    a = b
    b = inverte
    acerto = math.exp(a)
    bcerto = math.exp(b)
    ret = funcGeometrica(len(x), x, y, acerto, bcerto, parametro)
    ide = VerificaViabilidade(len(x), y, ret)
    if z == 'd' or z == 'D':
        print("TABELA DA FUNÇÃO Geométrica")
        for j in range(len(x)):
            if x[j] >= 0:
                print(f'  {x[j]:.3f} | {yge[j]:.3f} | {xy[j]:.3f}  | {xquad[j]:.3f}')
            else:
                print(f' {x[j]:.3f} | {yge[j]:.3f} | {xy[j]:.3f} | {xquad[j]:.3f}')
        if somax >= 0:
            print("Somatoria dos valores")
            print(f' x = {somax:.3f} |y = {somayge:.3f} | x*y = {somaxy:.3f}  | x^2 = {somaxquad:.3f}')
        else:
            print(f' {somax:.3f} | {somayge:.3f} | {somaxy:.3f}  | {somaxquad:.3f}')
        print('\n')
        print(f'a ={a} e b = {math.exp(b)}, o que forma a seguinte função: ', end='')
        print(f' {math.exp(b)} * x^({math.exp(a)})\n\n')
        print("o erro quadratico é de {} ".format(ide))
        print("e este é o gráfico: ")
        fig, ax = plt.subplots()
        plt.plot(x, y, label='Ideal')
        plt.plot(x, ret, label='Curva Geométrica')
        ax.legend()
        time.sleep(10)
        plt.show()

    return ret


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
    for _ in range(len(x)):
        if x[_] < 0:
            restraingeometric = True

    if restraingeometric:
        print("[A] Hiperbólica\n[B] Potencia\n[C] Exponencial\n[D] comparativo")
        z = input()
        if z == 'a' or z == 'A':
            TabHiperbolica(x, y, z)
        elif z == 'b' or z == 'B':
            TabPotencia(x, y, z)
        elif z == 'c' or z == 'C':
            tabExponencial(x, y, z)
        elif z == 'd' or z == 'D':
            variancia1, variancia2, i = 0, 0, 0
            potencia = TabPotencia(x, y, z)
            exponencial = tabExponencial(x, y, z)
            hiperbole = TabHiperbolica(x, y, z)
            plt.plot(x, y, label='Ideal')
            plt.plot(x, hiperbole, label='Curva Hiperbole')
            plt.plot(x, potencia, label='Curva Potencia')
            plt.plot(x, exponencial, label='Curva Exponencial')
            plt.legend()
            time.sleep(15)
            plt.show()
        else:
            break
    else:
        print("[A] Hiperbólica\n[B] Curva Exponencial\n[C] Exponencial\n[D] Geométrica\n[E] comparativo")
        z = input()
        if z == 'a' or z == 'A':

            TabHiperbolica(x, y, z)
        elif z == 'b' or z == 'B':
            TabPotencia(x, y, z)
        elif z == 'c' or z == 'C':
            tabExponencial(x, y, z)
        elif z == 'd' or z == 'D':
            tabGeometrica(x, y, z)
        elif z == 'e' or z == 'E':
            geometria = tabGeometrica(x, y, z)
            variancia1, variancia2, i = 0, 0, 0
            potencia = TabPotencia(x, y, z)
            exponencial = tabExponencial(x, y, z)
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

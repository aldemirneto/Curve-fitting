import math, time
import matplotlib.pyplot as plt

def VerificaViabilidade(tamanho, refy, real):
    soma = 0
    for i in range(tamanho):
        soma += ((refy[i] - real[i]) ** 2)
    decreta = (soma ** (1 / 2))
    return decreta


def funcExponencial(n, referenciax, a, b):
    exp = []
    for y in range(n):
        resultado = (b * math.exp(a * referenciax[y]))
        exp.append(resultado)
    return exp


def FuncHiperbolica(n, referenciax, a, b):
    hip = []
    for y in range(n):
        resultado = (1 / (a * referenciax[y] + b))
        hip.append(resultado)
    return hip


def FuncPotencia(n, referenciax, a, b):
    pot = []
    for l in range(0, n):
        resultant = (a * (b ** referenciax[l]))
        pot.append(resultant)
    return pot


def funcGeometrica(n, referenciax, a, b):
    geo = []
    for l in range(0, n):
        resultant = (a * (referenciax[l] ** b))
        geo.append(resultant)
    return geo


def Descobre_B(n, somax, somay, somaxy, somax2):
    resultado2 = (((somax * somaxy) - (somay * somax2)) / ((somax ** 2) - (n * somax2)))
    return resultado2


def Descobre_A(n, somax, somay, somaxy, somax2):
    resultado = (((n * somaxy) - (somax * somay)) / ((n * somax2) - (somax ** 2)))
    return resultado






def tabGeo(a, b, x, yge, xy, xquad, somax, somayge, somaxy, somaxquad, ide):
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





def plotCurva(x, y,ret, nome):    
    print(f"O grafico da função {nome} é: ")
    fig, ax = plt.subplots()
    plt.plot(x, y, label='Ideal')
    plt.plot(x, ret, label=f'Curva {nome}')
    ax.legend()
    time.sleep(10)
    plt.show()


def tabExpo(x, yexp, xy, xquad, somax, somayexp, somaxy, somaxquad, a, b, ide, retina):
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
    

def tabHiperbolica(x, yhip, xy, xquad, somax, somayhip, somaxy, somaxquad, a, b, ide, retorna):
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
 




def tabPotencia(x, yp, xy, xquad, somax, somayp, somaxy, somaxquad, a, b, i, retorn):
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
    print(f'a ={a} e b = {b}, o que forma a seguinte função: ', end='')
    print(f'\n {a} * {b}^x\n\n')
    print("o erro quadratico é de {}".format(i))



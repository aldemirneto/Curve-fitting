# Ajuste de Curvas

Este código tem como objetivo realizar o ajuste de curvas em um conjunto de dados. São utilizadas quatro funções diferentes para realizar o ajuste, sendo elas a função de potência, hiperbólica, exponencial e geométrica. O usuário é solicitado a inserir os valores de x e y que serão utilizados no ajuste.

## Tecnologias Utilizadas

- Python
- matplotlib



### Pré-requisitos

- math
- time
- matplotlib.pyplot
- functools

## Como utilizar

Para utilizar o código, basta executar o arquivo e inserir os valores de x e y quando solicitados.
Após isso, o usuário poderá escolher entre as quatro funções de ajuste disponíveis ou comparar todas elas em um mesmo gráfico.

## Funções
O código contém as seguintes funções:

- tpotencia: realiza o ajuste utilizando a função de potência;
- thiperbolica: realiza o ajuste utilizando a função hiperbólica;
- texponencial: realiza o ajuste utilizando a função exponencial;
- tgeometrica: realiza o ajuste utilizando a função geométrica.

## Exemplo:

Um exemplo de utilização:

```
Quantos pontos você quer inserir para o ajuste?
5
insira os valores de x
1
2
3
4
5
insira os valores de y
2
5
10
17
26
Qual aproximação você acha a mais adequada?
[A] Hiperbólica
[B] Curva Exponencial
[C] Exponencial
[D] Geométrica
[E] comparativo

ABELA DA FUNÇÃO EXPONENCIAL
  1.000 | 0.693 | 0.693  | 1.000
  2.000 | 1.609 | 3.219  | 4.000
  3.000 | 2.303 | 6.908  | 9.000
  4.000 | 2.833 | 11.333  | 16.000
  5.000 | 3.258 | 16.290  | 25.000
Somatoria dos valores
 x = 15.000 |y = 10.696 | x*y = 38.443  | x^2 = 55.000


a =0.6353674146545194 e b = 1.2626261142448199, o que forma a seguinte função:  1.2626261142448199 * e^(0.6353674146545194*x)


o erro quadratico é de 4.66929517680082
e o gráfico da função Exponencial é:
```
![image](https://user-images.githubusercontent.com/56364675/232336624-672ba544-2f12-4a78-89a1-0e652f04e635.png)


## Contribuição

Se você deseja contribuir para este projeto, siga os seguintes passos:

1. Faça um fork do repositório
2. Crie um branch com sua contribuição: `git checkout -b minha-contribuicao`
3. Realize as mudanças e faça o commit: `git commit -m 'Minha contribuição'`
4. Faça o push para o seu branch: `git push origin minha-contribuicao`
5. Crie um Pull Request no repositório original

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

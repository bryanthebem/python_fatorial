#9) Crie uma função recursiva que calcule o fatorial de um número n. A função deve retornar -1 caso não seja possível calcular o fatorial 
# Além disso, crie um algoritmo que leia um valor, utilize a função criada para calcular o fatorial e imprima o valor computado.

def fatorial(N):
    if N < 0:
        return -1
    elif N == 0 or N == 1:
        return 1
    else:
        return N * fatorial(N-1)

N = int(input('Digite o valor de N: '))
f = fatorial(N)
if f == -1:
    print('Não tem fatorial')
else:
    print('O Fatorial é: ', f)
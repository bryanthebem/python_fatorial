def fatorial(N):
    if N < 0:
        return -1
    elif N == 1:
        return 1
    else:
        return N * fatorial(N-1)

N = int(input('Digite seu numero: '))
x = fatorial(N)
if x == -1:
    print('Não é possivel calcular o fatorial')
else:
    print('Sua fatorial é', x)

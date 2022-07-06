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

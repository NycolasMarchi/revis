m = int(input('M:'))
n = int(input('N:'))
while True:
    if m==0 or n==0:
        print('Fim do programa.')
        break
    if m>n:
        s = list(range(n,m+1))
        soma = sum(s)
        print(s, 'Soma: ', soma)
        break
    elif m<n:
        s = list(range(m, n+1))
        soma = sum(s)
        print(s, 'Soma: ', soma)
        break



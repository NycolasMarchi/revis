while True:
    n = int(input('Digite um valor:'))
    if n>0:
        l = list(range(n+1))
        l.reverse()
        print(l)
        break
    else:
        print('Entrada invalida:')

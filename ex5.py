n = int(input('Digite um valor:'))
x = 0
y = 0
while n>0:
    x+=1
    n1 = float(input('Número {}:'.format(x)))
    if n1>0:
        y+=1
        n-=1
print(y, "valores são positivos")
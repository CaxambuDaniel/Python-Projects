n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma é {}, o produto é {},a divisão é {:.3f},'.format(s, m, d), end=' ')
print('a divisão inteira é {}, a potencia é {}'.format(di, e))

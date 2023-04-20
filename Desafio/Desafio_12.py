from math import sqrt
n1=float(input('De valor  do cateto oposto:'))
n2=float(input('De valor do cateto adjacente:'))
hip=sqrt((n1**2)+(n2**2))
print('Valor da hipotenusa é {:.2f}cm'.format(hip))
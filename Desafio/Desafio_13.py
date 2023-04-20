import math
co=float(input('De valor  do cateto oposto:'))
ca=float(input('De valor do cateto adjacente:'))
hip=math.hypot(co,ca)
print('A hipotenusa é {:.2f}cm'.format(hip))
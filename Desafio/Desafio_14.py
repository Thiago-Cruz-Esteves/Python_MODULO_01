import math
an=float(input('Digite o valor do ãngulo:'))
c=math.cos(math.radians(an))
s=math.sin(math.radians(an))
t=math.tan(math.radians(an))
print('O valo do coseno é de{:.2f}\nO valor de seno é de{:.2f}\nO valor de seno é de{:.2f}'.format(c,s,t))

from math import radians,sin,cos,tan
an=float(input('Valor do angulo?'))
s=sin(radians(an))
c=cos(radians(an))
t=tan(radians(an))
print('O valo do coseno é de {:.2f}\nO valor de seno é de {:.2f}\nO valor de seno é de {:.2f}'.format(c,s,t))
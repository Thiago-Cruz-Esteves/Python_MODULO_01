n1=int(input('Digite um numero:'))
n2=str(n1)
u=n1//1%10
d=n1//10%10
c=n1//100%10
m=n1//1000%10
print('Tem {} unidades'.format(u))
print('Tem {} dezenas'.format(d))
print('tem {} centenas'.format(c))
print('tem {} milhar'.format(m))
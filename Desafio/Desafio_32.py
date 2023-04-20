d=float(input('Qual distancia da sua viagem? '))
print('Você esta preste a fazer uma viagem de {}{:.2f}{}Km'.format('\033[34m',d,'\033[m'))
pre=d*0.50 if d<=200 else d*0.45
print('O preso da sua viagem é de R${:.2f}'.format(pre))
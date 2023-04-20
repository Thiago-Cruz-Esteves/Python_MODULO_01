d=float(input('Qual distancia da sua viagem? '))
print('Você esta preste a fazer uma viagem de {}Km'.format(d))
if d<200:
    v = d * 0.5
    print('O preso da sua viagem é de R${:.2f}'.format(v))
else:
    vd = d * 0.45
    print('O preso da sua viagem é de R${:.2f}'.format(vd))

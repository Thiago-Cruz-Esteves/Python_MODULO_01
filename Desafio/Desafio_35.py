s=float(input('Qula seu salario? '))
if s>=1200:
    v=s*1.10
    print('Que ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(s,v))
else:
    v1=s*1.15
    print('Que ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(s, v1))

ve=float(input('Qual a velosidade atual do seu carro? '))
if ve > 80: #as fomulas podem ser colocada dentro do if, só vão aprecer se o if for validado!
    print('MULTADO! Você exedeu o limite de velocidade que é 80Km/h')
    v1 = (ve - 80) * 7
    print('Voce devera pagar uma multa de R${:.2f}'.format(v1))
else:
    print('Tenha bom dia e dirija com segurança!')
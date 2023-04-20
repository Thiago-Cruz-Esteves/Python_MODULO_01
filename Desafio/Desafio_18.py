nome=str(input('Digite o seu nome completo: ')).strip()
dive=nome.split()
print('O seu nome em maiusculo fica {}'.format(nome.upper()))
print('O seu nome em minusculo fica {}'.format(nome.lower()))
print('O seu nome em completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu nome em completo tem {} letras.'.format(nome.find(' ')))
print('O seu primeiro nome tem {} letras.'.format(len(dive[0])))









#print('\033[0;;40mDite uma fraze?\033[m ')
nome='Thiago'
cores={'v':'\033[31m', 'ama':'\033[33m','az':'\033[34m', 'pb':'\033[7;30;m'}
cor=['\033[31m','\033[33m','\033[34m','\033[7;30;m']
print(f'Exemplo {cor[0]}{nome}{cor[3]}')
print(f'Exemplo {cores["ama"]}{nome}{cores["pb"]}')
print('Exemplo {} {} '.format(cores['ama'],nome))



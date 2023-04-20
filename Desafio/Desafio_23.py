frase=str(input('Digite uma frase:')).upper().strip()
print('\nA Palavra A foi digitada {} vezes na frase'.format(frase.count('A')))
print('A primeira letra é A aparece na posição {}'.format(frase.find('A')+1))
print('A  Ultima letra E foi digitada {} vezes na frase'.format(frase.rfind('A')+1))

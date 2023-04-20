pa=str(input('Digite a palavra: ')).upper().strip()
frase=str(input("""Digite uma frase:""")).upper().strip()
print('\nA Palavra {} foi digitada {} vezes na frase'.format(pa,frase.count(pa)))
print('A primeira a palavras {} aparece na posição {}'.format(pa,frase.find(pa)+1))
print('A  Ultima a palavras {} foi digitada na posição {} '.format(pa,frase.rfind(pa)+1))


from random import randint # randit e usado para numeros exp:(0,9999)
from time import sleep # tempo é usado adisonar tempo
comp=randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 a 5 tente adivinhar... ')
print('-=-'*20)
jo=int(input('Esconha um numero entre 0 e 5 ! '))
print('PROCESSANDO...')
sleep(2)# O sleep faz com que computador espere, mas tem que colocar quntidade de tempo em segundos!
if comp==jo:
    print('Parabenz! Voce venceu!')
else:
    print('Você pedeu, mas tente novamente!')

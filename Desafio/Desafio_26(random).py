import random
n=int(input('Esconha um numero entre 0 a 5: '))
n1=1
n2=2
n3=3
n4=4
n5=5
lt=[n1,n2,n3,n4,n5]
esco=random.choice(lt)
print('O numero que deu foi {}'.format(esco))
if n==esco:
    print('Você venceu!')
else:
    print('Você pedeu, mas tente novamente!')
print('-=-'*20)
print('Analize de triangulo')
print('-=-'*20)
a=float(input('Primeiro seguimento? '))
b=float(input('segundo seguimento? '))
c=float(input('terceiro seguimento? '))
if a<b+c and b<c+a and c<a+b :
    print("O valor dos seguimentos forman um triangulo")
else:
    print('O valores apresentado não forman o triangulo!')

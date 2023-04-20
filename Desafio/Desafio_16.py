import random
s1=str(input('nome do primeiro aluno?' ))
s2=str(input('nome do segundo aluno?' ))
s3=str(input('nome do terceiro aluno?' ))
s4=str(input('nome do quarto aluno?' ))
Lista=[s1,s2,s3,s4]
escolido=random.choice(Lista)
print('O aluno escolido foi {}'.format(escolido))
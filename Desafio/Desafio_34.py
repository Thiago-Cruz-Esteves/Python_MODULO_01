n=float(input('Digite um numero:  '))
n1=float(input('Digite um numero:  '))
n2=float(input('Digite um numero:  '))
menor=n
if n1<n and n1<c:
    menor=n1
if n2<n and n2<n1:
    menor=n2
print('O menor valor digitado foi {:.2f}'.format(menor))
maior=n1
if n>n1 and n>n2:
    maior=n
if n2>n and n2>n1:
    maior=n2
print('O valor maior é {}'.format(maior))
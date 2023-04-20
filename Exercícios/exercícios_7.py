d=float(input('Quantidade de dias alugado?'))
k=float(input('kilometragem percorida por automovel?'))
di=d*60
ki=k*0.15
vt=di+ki
print('O valor da diria é de R$:{:.2f}\nO valor da kilomeetrgem roda é de R$:{:.2f}\nO valor total é de R$:{:.2f}'.format(di,ki,vt))
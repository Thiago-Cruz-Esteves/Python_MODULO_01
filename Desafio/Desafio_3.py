medida: float=float(input(' Vlor em metros '))
m=medida
cm=medida*100
mm=medida*1000
km=medida/1000
print(' O valor em {:.2f}m coresponde:,\n Valor em {:.2f}km,\n Valor em {:.2f}cm,\n Valor em {:.2f}mm '.format(medida,km,cm,mm))
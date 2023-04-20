no=str(input('Digite seu nome completo:')).strip()
div=no.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}'.format(div[0]))
print('Seu ultimo nome é {}'.format(div[len(div)-1]))
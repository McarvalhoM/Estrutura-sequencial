sexo= str(input('Digite "m" se for homem ou "f" se for mulher'))
if sexo == 'm':
    h = float(input('digite sua altura'))
    homem = (72.7 * h) - 58
    print('seu peso ideal é', (homem), 'kg')
elif sexo == 'f':
    h = float(input('digite sua altura'))
    mulher = (62.1 * h) - 44.7
    print('seu peso ideal é', (mulher), 'kg')
else:
    print('Digite um sexo e/ou idade correta')

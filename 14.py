#se joao pescar mais de 50kg, paga multa de 4 reais por kg em excesso
#>> mostrar quantos kg de peixe total
#>> mostrar quantos kg de excesso
#>> mostrar quanto de multa joao ira pagar

pescado= float(input('Digite o valor que Joao pescou'))
if pescado <= 50:
    print('joao pescou', pescado, 'kg de peixe')
    print('joao nao pescou em excesso, portanto, nao pagara multa')
else:
    excesso= float((pescado - 50))
    multa= (excesso*4)
    print('joao pescou', pescado, 'kg de peixe')
    print('joao pescou', excesso, 'kg de peixe em excesso')
    print('joao ira pagar', multa, 'R$ de multa')

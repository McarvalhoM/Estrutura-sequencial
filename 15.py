gh = float(input('quanto você ganha por hora'))
ht = int(input('quantas horas voce trabalha por mes'))
t = (gh * ht)
print('você ganha', t, 'R$, mas...')
print('Você ainda irá pagar impostos...')
ir = (t/100)*11
inss = (t/100)*8
sind = (t/100)*5
liquido = (t-ir-inss-sind)
print('Você no final de tudo pagou:', ir, 'R$ de imposto de renda; ', inss, 'R$ de INSS; ', sind, 'R$ para o sindicato'
      ' e no total ganhou', liquido, 'R$ liquido')

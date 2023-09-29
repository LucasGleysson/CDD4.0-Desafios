# Exercicio 11 do slide
# Receber a idade, o mês e o dia de uma pessoa e calcular a quantos dias ela está viva.

idade = int(input('Digite a idade: '))
mes = int(input('Digite o mês: '))
dia = int(input('Digite a dia: '))

dias_ano = idade * 365
dias_mes = mes * 30
dias_vivo = dias_ano + dias_mes + dia

print(f'{dias_vivo} vivo. PARABENS! amanhã tem mais.')
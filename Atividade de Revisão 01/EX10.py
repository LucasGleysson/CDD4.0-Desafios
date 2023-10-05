# Exercicio 16 do slide
# Calculo de horas

h_inicial = int(input('Digite a hora inteira de inicio do jogo: '))
h_final = int(input('Digite a hora inteira de inicio do jogo: '))
h_total = h_final - h_inicial

if h_final <= h_inicial:
    resto = 24 - h_inicial
    h_total = h_final + resto

print(f'A partida durou: {h_total}')

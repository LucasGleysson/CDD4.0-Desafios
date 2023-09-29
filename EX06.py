# Exercicio 12 do slide
# Receber a quantidade de votos nulos, validos e brancos e mostrar a porcentagem

votos_validos = int(input('Digite a quantidade de votos validos: '))
votos_brancos = int(input('Digite a quantidade de votos brancos: '))
votos_nulos = int(input('Digite a quantidade de votos nulos: '))

eleitores_total = votos_nulos + votos_brancos + votos_validos

p_validos = (votos_validos / eleitores_total) * 100
p_brancos = (votos_brancos / eleitores_total) * 100
p_nulos = (votos_nulos / eleitores_total) * 100

print(f'Votos Validos: {p_validos:.1f}%')
print(f'Votos Brancos: {p_brancos:.1f}%')
print(f'Votos Nulos: {p_nulos:.1f}%')

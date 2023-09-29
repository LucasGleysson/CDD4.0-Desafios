# Exercicio 14 do slide
# Cria um conversor de F° para C°

f = float(input('Digite a temperatura em F°: '))
c = ((f - 32) / 9) * 5

print(f'{f:.0f}F° é equivalente a {c:.0f}C°')

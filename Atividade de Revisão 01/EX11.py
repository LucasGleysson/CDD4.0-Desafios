# Exercicio 17 do slide
# Calcular o preço de maçãs

qnt_maca = int(input('Digite a quantiadde maçãs compradas: '))

if qnt_maca >= 12:
    preco = 1
else:
    preco = 1.30

valor_compra = qnt_maca * preco
print(f'Valor total: R${valor_compra}')

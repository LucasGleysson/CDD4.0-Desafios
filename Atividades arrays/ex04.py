numeros = [0]*30
qnt_pares, maior, menor, soma = 0, 0, 0, 0

for i in range(30):
    numeros[i] = int(input(f"Digite o {i+1}º numero: "))
    soma += i

    if numeros[i] % 2 == 0:
        qnt_pares += 1

    if i == 0:
        maior = numeros[i]
        menor = numeros[i]
    else:
        if maior < numeros[i]:
            maior = numeros[i]
        if menor > numeros[i]:
            menor = numeros[i]

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')

print('Os números PARES digitados são: ')

media = soma / 30
qnt_media = 0
for i in numeros:
    if i > media:
        qnt_media += 1
    if i % 2 == 0:
        print(i, end=' ')

print(f'\nQuantidade de valores maior que a média: {qnt_media}')

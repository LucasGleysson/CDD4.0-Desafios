# Exercicio 10 do slide
qnt = int(input('Digite o tamanho do array: '))

arrayA = [0] * qnt
arrayB = [0] * qnt
arraySoma = [0] * qnt

for indice in range(qnt):
    arrayA[indice] = int(input('Digite um número para A: '))
    arrayB[indice] = int(input('Digite um número para B: '))
    arraySoma[indice] = arrayA[indice] + arrayB[indice]

print(arrayA)
print(arrayB)
print(arraySoma)

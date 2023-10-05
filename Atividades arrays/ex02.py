# Exercicio 11

# POPULA O VETOR
vetor = [0]*30
for i in range(30):
    vetor[i] = int(input(f'Digite o {i+1} valor: '))

# RECEBE E BUSCA O NÚMERO NO VETOR
num = int(input('Digite o numero que será encontrado: '))
contador = 0
for j in range(30):
    if vetor[j] == num:
        contador += 1

# MOSTRA O RESULTADO
if contador == 0:
    print('Este número não existe no vetor.')
else:
    print(f'O número {num} foi encontrado {contador} VEZES no vetor.')

# Exercicio 08 do slide
# Receber números e exibir a soma e a média

qnt = int(input('Digite a quantidade de números que serão calculados: '))
soma = 0

for i in range(qnt):
    num = float(input(f'Digite o {qnt+1}º número: '))
    soma += num

media = soma / qnt
print(f'A soma dos números digitados é {soma}')
print(f'A média dos números é: {media}')

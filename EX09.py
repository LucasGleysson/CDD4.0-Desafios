# Exercicio 15 do slide
# Números em ordem crescente

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

while num1 == num2:
    print('Os valores não podem ser iguais!')
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))

if num1 < num2:
    print(f'1Em ordem crescente os valores são {num1} e {num2}')
else:
    print(f'Em ordem crescente os valores são {num2} e {num1}')

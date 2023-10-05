nomes = ['']*5
for i in range(5):
    nomes[i] = input(f"Digite o {i+1}º nome: ")

print("======= Ordem de entrada =======")
for nome in nomes:
    print(f"- {nome}")

print('======= Ordem inversa =======')
for indice in range(4, -1, -1):
    print(f"- {nomes[indice]}")

menu = """ MENU
1 - CRIAR
2 - VIZUALIZAR
3 - ATUALIZAR
4 - DELETAR
0 - SAIR

opção: """

menu_tabelas = """MENU
1 - ALUNO
2 - FUNCIONARIO
3 - PERSONAL
4 - MODALIDADE
0 - VOLTAR

opção: """
op_menu = input(menu)
def op_tabela(op_menu):
    ...


while True:
    op_menu = input(menu)

    if op_menu not in "12340":
        print("Opção invalida! Escolha entre as opções na tela.")
        continue
    if op_menu == "0":
        break
    elif op_menu == "1":
        ...

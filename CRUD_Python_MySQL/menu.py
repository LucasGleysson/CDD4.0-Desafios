import database

menu = """- CRIAR
- VIZUALIZAR
- ATUALIZAR
- DELETAR
- VOLTAR

opção: """

menu_tabelas = """=========TABELAS=========
- ALUNOS
- FUNCIONARIO
- PERSONAL
- MODALIDADES
- SAIR

opção: """


while True:
    op_tab_validas = ["alunos", "funcionario", "personal", "modalidades", "sair"]
    op_menu_tabela = input(menu_tabelas).lower().strip()
    if op_menu_tabela not in op_tab_validas:
        print("Opção invalida! Verifique a resposta passada e tente novamente.")
        continue
    elif op_menu_tabela == "sair":
        break
    else:
        print("=" * 26)
        print(f"TABELA: {op_menu_tabela.upper()}")
        op_men_validas = ["criar", "vizualizar", "atualizar", "deletar", "voltar"]
        op_menu = input(menu).lower().strip()
        if op_menu not in op_men_validas:
            print("Opção invalida! Verifique a resposta passada e tente novamente.")
            continue
        elif op_menu == "voltar":
            continue

        if op_menu == "criar":
            novo_id = database.creater(op_menu_tabela)
            print(f"Cadastro efetuado! Novo ID: {novo_id}")
        elif op_menu == "vizualizar":
            database.reader(op_menu_tabela)
        elif op_menu == "deletar":
            database.delete(op_menu_tabela)

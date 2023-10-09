tamanho = 2
vetor_usuarios = [''] * tamanho
vetor_senhas = [''] * tamanho

print("=" * 20)
print("CADASTRO")
print("=" * 20)

for i in range(tamanho):
    vetor_usuarios[i] = input('Insira o nome do usuário: ')
    vetor_senhas[i] = input('Digite a senha: ')

print("=" * 20)
print("LOGIN")
print("=" * 20)

log_user_ok = False
log_senha_ok = False
i = 0
tentativas = 0

# Enquanto o usuário não for validado, pede o usurário
while not log_user_ok:
    log_usuario = input('Insira o nome do usuario: ')
    for i in range(tamanho):
        if vetor_usuarios[i] == log_usuario:
            log_user_ok = True
            break

    # Se o usuário não for validado, perde uma tentativa
    if not log_user_ok:
        print('Usuário Invalido!')
        tentativas += 1

    # Se passar de três tentativas o programa é encerrado
    if tentativas == 3:
        log_senha_ok = "Erro"
        print("FINALIZADO")
        break

    # Se o usuário for validado e a senha ainda estiver pendente, solicita a senha
    while log_user_ok and not log_senha_ok:
        log_senha = input('Digite a senha: ')
        if log_senha == vetor_senhas[i]:
            log_senha_ok = True
            print("Login Efetuado com SUCESSO")
            break
        else:
            print('Senha invalida')
            tentativas += 1

        # Se a senha for errada três vezes, ela será recadastrada e o processo de login começa novamente.
        if tentativas == 3:
            print("RECADASTRAR SENHA!")
            vetor_senhas[i] = input('Digite a nova senha: ')
            print("REALIZE O LOGIN")
            tentativas = 0
            log_user_ok = False
            log_senha_ok = False
            break

        # Se tiver tudo OK mostra os dados do usuário logado
        if log_user_ok and log_senha_ok:
            print('=' * 20)
            print(f'ID: {i}')
            print(f'USUARIO: {vetor_usuarios[i]}')
            print(f'SENHA: {vetor_senhas[i]}')
            print('=' * 20)

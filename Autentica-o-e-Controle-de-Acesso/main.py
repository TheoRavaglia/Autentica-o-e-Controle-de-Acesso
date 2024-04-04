import getpass

while tentativas < tentativas_max:
    print("1. Entrar com uma conta existente")
    print("2. Criar uma nova conta")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        email = input("Digite seu email: ")
        senha = getpass.getpass("Digite sua senha: ")

        usuario = None
        error = None
        try:
            usuario = auth.sign_in_with_email_and_password(email, senha)
            print("Tipo de usuario:", type(usuario))  
            print("Usuario:", usuario) 
            
            id = usuario['idToken']
            
            usuario_info = auth.get_account_info(id)

            redefinir_senha = input("Deseja redefinir a senha? (s/n): ")
            if redefinir_senha.lower() == 's':
                auth.send_password_reset_email(email)
                print("E-mail de redefinição de senha enviado para:", email)

        except Exception as e:
            error = e
        
        if usuario is not None: #autenticacao deu certo
            break
        else:
            tentativas += 1
            print("Falha na autenticação:", error)
            if tentativas < tentativas_max:
                print("Tentativa", tentativas, "de", tentativas_max)
            else:
                print("Tentativas demais!")
                break
                
    elif opcao == "2":
        email = input("Digite o novo email: ")
        senha = getpass.getpass("Digite a nova senha: ")
        
        try:
            token = auth.create_user_with_email_and_password(email, senha)
            print("Usuário criado com sucesso!")
            
            auth.send_email_verification(token['idToken'])
            print("E-mail de verificação enviado para:", email)
            
            break
        except Exception as e:
            print("Erro ao criar usuário:", e)
            continue
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
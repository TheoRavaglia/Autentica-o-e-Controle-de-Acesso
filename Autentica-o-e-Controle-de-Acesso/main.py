##Otavio Murilo
##Theo Machado

import getpass
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

while True:
    print("1. Entrar com uma conta existente")
    print("2. Criar uma nova conta")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        email = input("Digite seu email: ")
        senha = getpass.getpass("Digite sua senha: ")

        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            usuario_registrado = False
            for linha in usuarios:
                dados = linha.strip().split(",")
                if email == dados[0] and hash_senha(senha) == dados[1]:
                    usuario_registrado = True
                    print("Autenticação bem-sucedida.")
                    break
                    
            if not usuario_registrado:
                print("Falha. Usuário ou senha inválidos.")

    elif opcao == "2":
        email = input("Digite o novo email: ")
        senha = getpass.getpass("Digite sua senha: ")
        senha_hash = hash_senha(senha)

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{email},{senha_hash}\n")
            print("Usuário registrado com sucesso!")

    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

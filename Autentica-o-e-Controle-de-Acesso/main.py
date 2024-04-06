##Otavio Murilo
##Theo Machado

import getpass
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def acoes():
    while True:
        print("===========")
        print("1. Listar Arquivo")
        print("1. Criar Arquivo")
        print("1. Ler Arquivo")
        print("1. Excluir Arquivo")
        print("2. Executar arquivo")
        print("3. Sair")
        print("===========")
        acao = input("Escolha uma opção: ")



while True:
    print("===========")
    print("1. Entrar com um perfil existente")
    print("2. Criar um novo perfil")
    print("3. Sair")
    print("===========")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")

        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            usuario_registrado = False
            for linha in usuarios:
                dados = linha.strip().split(",")
                if nome == dados[0] and hash_senha(senha) == dados[1]:
                    usuario_registrado = True
                    print("Autenticação bem-sucedida.")
                    print("Bem vindo", nome)
                    acoes()
                    break
                    
            if not usuario_registrado:
                print("Usuário ou senha inválidos.")

    elif opcao == "2":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")
        senha_hash = hash_senha(senha)

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome}, Senha: {senha_hash}\n")
            print("Usuário registrado com sucesso!")

    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

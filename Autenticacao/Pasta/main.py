##Otavio Murilo
##Theo Machado

import getpass
import hashlib
import os

def hash_senha(senha): ##Criptografia das senhas usando hashlib
    return hashlib.sha256(senha.encode()).hexdigest()

def listagem_arquivo():    
    try:
        files = os.listdir()
        print("Arquivos no diretório:")
        for file in files:
            print(file)
    except Exception as e:
        print(f"Ocorreu um erro ao listar os arquivos: {e}")

def criar_arquivo():
    fileName = input("Digite o nome do arquivo: ")
    conteudo = input("Digite o conteúdo do arquivo: ")
    
    with open(fileName, 'w') as arquivo:
        arquivo.write(conteudo)
    
    print(f"Arquivo '{fileName}' criado com sucesso!")



def acoes(): ##Tela apos o login realizado com sucesso
    while True:
        print("===========")
        print("1. Listar Arquivo")
        print("2. Criar Arquivo")
        print("3. Ler Arquivo")
        print("4. Excluir Arquivo")
        print("5. Executar arquivo")
        print("6. Sair")
        print("===========")
        acao = input("Escolha uma opção: ")
        
        if acao == "1":
            listagem_arquivo()
        elif acao == "2":
            criar_arquivo()
        
        elif acao == "6":
            print("Sessão encerrada")
            break

        else:
            print("Opção inválida.")



while True:  ##Menu inicial
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
            registro = False
            for linha in usuarios:
                dados = linha.strip().split(",")
                if nome == dados[0] and hash_senha(senha) == dados[1]:
                    registro = True
                    print("Autenticação bem-sucedida.")
                    acoes()
                    break
                    
            if not registro:
                print("Usuário ou senha inválidos.")

    elif opcao == "2":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")
        senha_hash = hash_senha(senha)

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome},{senha_hash}\n")
            print("Usuário registrado com sucesso!")

    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

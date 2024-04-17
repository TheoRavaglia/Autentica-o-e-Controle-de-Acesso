##Otavio Murilo
##Theo Machado

import getpass
import hashlib
import os
import subprocess

def hash_senha(senha): 
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_cadastro(nome, usuarios):
    with open(usuarios, "r") as arquivo:
        for linha in arquivo:
            if nome in linha:
                return True
    return False                    

def listagem_arquivo():    
        arquivo = os.listdir()
        print("Arquivos no diretório:")
        for file in arquivo:
            print(file)

def criar_arquivo():
    fileName = input("Digite o nome do arquivo: ")
    conteudo = input("Digite o conteúdo do arquivo: ")
    with open(fileName, 'w') as arquivo:
        arquivo.write(conteudo)
    
    print(f"Arquivo '{fileName}' criado.")

def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
    try:
        with open("permissoes.txt", "r") as permissao_arquivo:
            permissoes = permissao_arquivo.readlines()
            for linha in permissoes:
                dados = linha.strip().split(",")
                if nome == dados[0]:
                    if int(dados[2]) == 1:
                        subprocess.run(["xdg-open", nome_arquivo])  # Linux com xdg-open
                        # subprocess.run(["open", nome_arquivo])  # macOS
                        # subprocess.run(["start", nome_arquivo], shell=True)  # Windows
                        return
                    else:
                        print("Você não tem permissão para ler arquivos.")
                        return
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def excluir_arquivo():
    fileName = input("Digite o nome do arquivo que deseja excluir: ")
    try:
        with open("permissoes.txt", "r") as permissao_arquivo:
            permissoes = permissao_arquivo.readlines()
            for linha in permissoes:
                dados = linha.strip().split(",")
                if nome == dados[0]:
                    if int(dados[3]) == 1:  # Verifica se o usuário tem permissão para excluir arquivos
                        os.remove(fileName)
                        print(f"Arquivo '{fileName}' excluído com sucesso.")
                        return
                    else:
                        print("Você não tem permissão para excluir arquivos.")
                        return
        print("Usuário não encontrado.")
    except FileNotFoundError:
        print("Erro.")

def executar_arquivo():
    fileName = input("Digite o nome do arquivo que deseja executar: ")
    try:
        with open("permissoes.txt", "") as permissao_arquivo:
            permissoes = permissao_arquivo.readlines()
            for linha in permissoes:
                dados = linha.strip().split(",")
                if nome == dados[0]:
                    if int(dados[2]) == 1:  # Verifica se o usuário tem permissão para executar arquivos
                        subprocess.run(["python", fileName])
                        return
                    else:
                        print("Você não tem permissão para executar arquivos.")
                        return
        print("Usuário não encontrado.")
    except FileNotFoundError:
        print("Arquivo de permissões não encontrado.")

def acoes(): ##Tela apos o login realizado com sucesso
    while True:
        print("===========")
        print("1. Listar Arquivo")
        print("2. Criar Arquivo")
        print("3. Ler Arquivo")
        print("4. Excluir Arquivo")
        print("5. Executar arquivo")
        print("6. Encerrar sessão")
        print("===========")
        acao = input("Escolha uma opção: ")
        
        if acao == "1":
            listagem_arquivo()
        elif acao == "2":
            criar_arquivo()
        elif acao == "3":
            ler_arquivo()
        elif acao == "4":
            excluir_arquivo()
        elif acao == "5":
            executar_arquivo()
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
                print("Usuário ou senha inválidos. Por favor, tente novamente.")
                continue  # Volta ao início do loop para que o usuário escolha outra opção

    elif opcao == "2":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")
        senha_hash = hash_senha(senha)

        if verificar_cadastro(nome, "usuarios.txt"):
            print("Nome de usuário já cadastrado")
                        
        else:   
            with open("usuarios.txt", "a") as arquivo:    
                    arquivo.write(f"{nome},{senha_hash}\n")
            print("Usuário registrado com sucesso")

        with open("permissoes.txt", "a") as permissao:
            permissao.write(f"{nome},{'0'},{'0'},{'0'}\n")
            
    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

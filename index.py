# Declaracao Variaveis
codigo = 0
nome = ""
tipo = 0
preco = 0
venda = False

series = []
serie = []
filmes = []
filme = []
documentarios = []
documentario = []

# Declaracao das Funcoes


def cadastro(codigo, nome, tipo, preco, venda):
    codigo -= 1
    produtos = []

    produtos.insert(0, f"Código: {codigo}")
    produtos.insert(1, f"Nome: {nome}")
    produtos.insert(2, f"Tipo: {tipo}")
    produtos.insert(3, f"Preço: {preco}")
    produtos.insert(4, f"Disponibilidade de Venda: {venda}")

    return produtos


def Tipos():
    print("1 - Série\n 2 - Filme\n 3 - Documentário")
    print("Digite o número")


def Tarefa():
    print("1 - Cadastro\n 2 - Consulta\n 3 - Atualizar\n 4 - Relatório\n 5 - Registro de Compra\n 6 - Relatório de Compra\n 7 - Sair")
    print("Digite o número")


def Informacoes():
    print("1 - Nome\n 3 - Preço\n 4 - Diponibilidade para Venda")
    print("Digite o número")
# Inicio do Codigo


print("Bem Vindo (a) ao NerdFlix")

while True:
    print("Escolha uma opção \n")
    Tarefa()
    opTarefa = int(input("Escolha uma opção acima: "))
    while opTarefa <= 0:
        print("Opção inválida!! \n Vamos tentar novamente!")
        Tarefa()
        opTarefa = int(input("Escolha uma opção acima: "))

    if opTarefa == 1:  # Tarefa 1 Cadastro

        print("< Cadastro de Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0:
            print("Opção inválida!! \n Vamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:
            print("< Cadastro de Séries />")

            print("Iformações do Produto \n")
            codigo += 1
            nome = input("Nome: ")
            tipo = 1
            preco = float(input("Preço: "))
            venda = bool(input("Disponibilidade para venda: "))

            serie = cadastro(codigo, nome, tipo, preco, venda)
            series += [serie]
            print("Série cadastrada com sucesso!")

        elif opTipo == 2:
            print("< Cadastro de Filmes />")

            print("Iformações do Produto")
            codigo += 1
            nome = input("Nome: ")
            tipo = 2
            preco = float(input("Preço: "))
            venda = bool(input("Disponibilidade para venda: "))

            filme = cadastro(codigo, nome, tipo, preco, venda)
            filmes += [filme]
            print("Filme cadastrado com sucesso!")

        elif opTipo == 3:
            print("< Cadastro de Documentários />")

            print("Iformações do Produto")
            codigo += 1
            nome = input("Nome: ")
            tipo = 3
            preco = float(input("Preço: "))
            venda = bool(input("Disponibilidade para venda: "))

            documentario = cadastro(codigo, nome, tipo, preco, venda)
            documentarios += [documentario]
            print("Documentário cadastrado com sucesso!")

    elif opTarefa == 2:  # Tarefa 2 Consulta

        print("< Consulta de Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0:
            print("Opção inválida!! \n Vamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Consulta de Série
            print("Séries cadastradas:")
            print(series)

        elif opTipo == 2:  # Consulta de Filmes
            print("Filmes cadastrados:")
            print(filmes)

        elif opTipo == 3:  # Consulta de Documentários
            print("Filmes documentários:")
            print(documentarios)

    elif opTarefa == 3:  # Tarefa 3 Atualizar

        print("< Atualizar Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0:
            print("Opção inválida!! \n Vamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Atualizar Série
            print("Lista de séries cadastradas:")
            print(series)

            codSerie = int(input("Informe o código: "))
            while codSerie < 0:
                print("Opção inválida!! \n Vamos tentar novamente!")
                print("Lista de séries cadastradas:")
                print(series)
                codSerie = int(input("Escolha uma opção acima: "))

            serieSelect = series[codSerie]

            print(f"Série informada {serieSelect}")

            print("Selecione o que iremos alterar")
            Informacoes()
            codInfo = int(input("Escolha uma opção acima: "))
            while codInfo < 0:
                print("Opção inválda!! \n Vamos tentar novamente!")
                Informacoes()
                codInfo = int(input("Escolha uma opção acima: "))

            date = input("Informe o dado alterado: ")

            serieSelect[codInfo] = date

            print("Dado alterado com sucesso!")

        elif opTipo == 2:  # Atualizar Filme

            print("Lista de filmes cadastradas:")
            print(filmes)

            codFilme = int(input("Informe o código: "))
            while codFilme < 0:
                print("Opção inválida!! \n Vamos tentar novamente!")
                print("Lista de filmes cadastradas:")
                print(filmes)
                codFilme = int(input("Escolha uma opção acima: "))

            filmeSelect = filmes[codFilme]

            print(f"Filme informado {filmeSelect}")

            print("Selecione o que iremos alterar")
            Informacoes()
            codInfo = int(input("Escolha uma opção acima: "))
            while codInfo < 0:
                print("Opção inválda!! \n Vamos tentar novamente!")
                Informacoes()
                codInfo = int(input("Escolha uma opção acima: "))

            date = input("Informe o dado alterado: ")

            filmeSelect[codInfo] = date

            print("Dado alterado com sucesso!")

        elif opTipo == 3:  # Atualizar Documentário
            print("Lista de documentários cadastradas:")
            print(documentarios)

            codDocumentario = int(input("Informe o código: "))
            while codDocumentario < 0:
                print("Opção inválida!! \n Vamos tentar novamente!")
                print("Lista de documentários cadastradas:")
                print(documentarios)
                codDocumentario = int(input("Escolha uma opção acima: "))

            documentariosSelect = documentarios[codDocumentario]

            print(f"Filme informado {documentariosSelect}")

            print("Selecione o que iremos alterar")
            Informacoes()
            codInfo = int(input("Escolha uma opção acima: "))
            while codInfo < 0:
                print("Opção inválda!! \n Vamos tentar novamente!")
                Informacoes()
                codInfo = int(input("Escolha uma opção acima: "))

            date = input("Informe o dado alterado: ")

            documentariosSelect[codInfo] = date

            print("Dado alterado com sucesso!")

    elif opTarefa == 7:
        print("Saindo do NerdFlix")
        break

import datetime

# Declaracao Variaveis
nome = ""
tipo = 0
preco = 0
venda = False

series = []
serie = []
codSerie = 0

filmes = []
filme = []
codFilme = 0

documentarios = []
documentario = []
codDocumentario = 0

codigoCliente = 0
nomeCliente = ""

cliente = []
clientes = []

compra = []
compras = []
codigoCompra = []

# Declaracao das Funcoes


def dataAtual():
    hoje = datetime.date.today()
    return hoje


def cadastro(codigo, nome, tipo, preco, venda):
    codigo -= 1
    produtos = []

    produtos.insert(0, f"Código: {codigo}")
    produtos.insert(1, f"Nome: {nome}")
    produtos.insert(2, f"Tipo: {tipo}")
    produtos.insert(3, f"Preço: {preco}")
    produtos.insert(4, f"Disponibilidade de Venda: {venda}")

    return produtos


def cadastroCliente(codigoCliente, nomeCliente):
    codigoCliente -= 1
    clientes = []

    clientes.insert(0, f"Código: {codigoCliente}")
    clientes.insert(1, f"Nome Cliente: {nomeCliente}")

    return clientes


def cadastroCompra(codigoCompra, nomeCliente, codigoProduto, preco, dataCompra):
    codigoCompra -= 1
    compras = []

    dataCompra = dataAtual()

    compras.insert(0, f"Código: {codigoCompra}")
    compras.insert(1, f"Nome: {nomeCliente}")
    compras.insert(2, f"Produto: {codigoProduto}")
    compras.insert(3, f"Preço: {preco}")
    compras.insert(4, f"Data da Compra: {dataCompra}")

    return compras


def Tipos():
    print("|1 - Série| |2 - Filme| |3 - Documentário|")
    print("Digite o número")


def TiposPlusClientes():
    print("|1 - Série| |2 - Filme| |3 - Documentário| |4 - Clientes|")
    print("Digite o número")


def TiposRelatorio():
    print("|0 - Todos os Produtos| |1 - Filmes| |2 - Séries| |3 - Documentários| |4 - Disponíveis para Venda| |5 - Indiponível para Venda|")
    print("Digite o número")


def Tarefa():
    print("|1 - Cadastro| |2 - Consulta| |3 - Atualizar| |4 - Relatório| |5 - Registro de Compra| |6 - Relatório de Compra| |7 - Registro de Clientes| |8 - Sair|")
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
            codSerie += 1
            nome = input("Nome: ")
            tipo = 1
            preco = float(input("Preço: "))
            venda = input("Disponibilidade para venda: ")

            serie = cadastro(codSerie, nome, tipo, preco, venda)
            series += [serie]
            print("Série cadastrada com sucesso!")

        elif opTipo == 2:
            print("< Cadastro de Filmes />")

            print("Iformações do Produto")
            codFilme += 1
            nome = input("Nome: ")
            tipo = 2
            preco = float(input("Preço: "))
            venda = input("Disponibilidade para venda: ")

            filme = cadastro(codFilme, nome, tipo, preco, venda)
            filmes += [filme]
            print("Filme cadastrado com sucesso!")

        elif opTipo == 3:
            print("< Cadastro de Documentários />")

            print("Iformações do Produto")
            codDocumentario += 1
            nome = input("Nome: ")
            tipo = 3
            preco = float(input("Preço: "))
            venda = input("Disponibilidade para venda: ")

            documentario = cadastro(codDocumentario, nome, tipo, preco, venda)
            documentarios += [documentario]
            print("Documentário cadastrado com sucesso!")

    elif opTarefa == 2:  # Tarefa 2 Consulta

        print("< Consulta de Produtos />")

        TiposPlusClientes()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0:
            print("Opção inválida!! \n Vamos tentar novamente!")
            TiposPlusClientes()
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

        elif opTipo == 4:  # Consulta de Clientes
            print("Clientes Cadastrados")
            print(clientes)
        else:
            print("Produto não cadastrado")

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

    elif opTarefa == 4:  # Tarefa 4 Relatório
        print("< Relatório />")

        TiposRelatorio()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo < 0:
            print("Opção Inválida! \n Vamos tentar novamente!")
            TiposRelatorio()
            opTipo = int(input("Escolha uma opção acima:"))

        if opTipo == 0:  # Todos os Produtos
            print("Todos os Produtos")
            print(f"Filmes: {filmes}")
            print(f"Séries: {series}")
            print(f"Documentários: {documentarios}")

        elif opTipo == 1:  # Todos os Filmes
            print("Todos o filmes")
            print(f"Filmes: {filmes}")

        elif opTipo == 2:  # Todas as Séries
            print("Todos o séries")
            print(f"Séries: {series}")

        elif opTipo == 3:  # Todos os Documentários
            print("Todos o documentários")
            print(f"Documentários: {documentarios}")

        elif opTipo == 4:  # Todos Diponíveis
            todosProdutos = series + filmes + documentarios
            totalProdutos = len(todosProdutos)
            true = []
            for i in range(totalProdutos):
                produto = todosProdutos[i]
                teste = produto[4]
                if teste == 'Disponibilidade de Venda: True':
                    true += [produto]

            print("Produtos disponíveis para venda")
            print(f"{true}")

        elif opTipo == 5:  # Todos Indiponíveis
            todosProdutos = series + filmes + documentarios
            totalProdutos = len(todosProdutos)
            false = []
            for i in range(totalProdutos):
                produto = todosProdutos[i]
                teste = produto[4]
                if teste == 'Disponibilidade de Venda: False':
                    false += [produto]

            print("Produtos indiponíveis para venda")
            print(f"{false}")

    elif opTarefa == 5:  # Tarefa 5 Registro de Compra
        print("< Registro de Compras />")

        totalClientes = len(clientes)
        if totalClientes == 0:
            print("Nenhum cliente cadastrado ainda!")
            print("Acesso a opção 7 do menu anterior")
            print("Saindo...")
        else:
            print("Informe um cliente")
            print("Clientes cadastrados: ")
            print(clientes)

            totalClientes = len(clientes)

            codCliente = int(input("Informe o código: "))
            while codCliente < 0:
                print("Opção inválda!! \n Vamos tentar novamente!")
                Informacoes()
                codCliente = int(input("Escolha uma opção acima: "))

            clienteSelect = clientes[codCliente]
            print(f"Cliente selecionado: {clienteSelect[1]}")

            print("Selecione o item para a compra: ")

            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))
            while opTipo <= 0:
                print("Opção inválda!! \n Vamos tentar novamente!")
                Tipos()
                opTipo = int(input("Escolha uma opção acima: "))

            tamanhoSerie = len(series)
            tamanhoFilme = len(filmes)
            tamanhoDocumentario = len(documentarios)

            if opTipo == 1:  # Compra de Séries
                if tamanhoSerie > 0:
                    print("< Compra de Séries />")

                    print(f"Séries: {series}")
                    codSerie = int(input("Informe o código da série: "))
                    serieSelect = series[codSerie]
                    while codSerie < 0:
                        print("Opção inválda!! \n Vamos tentar novamente!")
                        print(f"Séries: {series}")
                        codSerie = int(input("Informe o código da série: "))
                        serieSelect = series[codSerie]

                    dispCompra = serieSelect[4]

                    while dispCompra == "Disponibilidade de Venda: False":
                        print(
                            "Opção não disponível para venda, vamos tentar novamente")
                        print(f"Séries: {series}")
                        codSerie = int(input("Informe o código da série: "))
                        serieSelect = series[codSerie]
                        dispCompra = serieSelect[4]

                    print(f"Séria selecionada: {serieSelect[1]}")

                else:
                    print("Nenhuma série cadastrada ainda!")
                    print("Retorno no menu anterior e cadastre uma série")

            elif opTipo == 2:  # Compra de Filmes
                if tamanhoFilme > 0:
                    print("< Compra de Filmes />")

                    print(f"Filmes: {filmes}")
                    codFilme = int(input("Informe o código do filme: "))
                    filmeSelect = filmes[codFilme]
                    while codFilme < 0:
                        print("Opção inválda!! \n Vamos tentar novamente!")
                        print(f"Filmes: {filmes}")
                        codFilme = int(input("Informe o código do filme: "))
                        filmeSelect = filmes[codFilme]

                    dispCompra = filmeSelect[4]

                    while dispCompra == "Disponibilidade de Venda: False":
                        print(
                            "Opção não disponível para venda, vamos tentar novamente")
                        print(f"Filmes: {filmes}")
                        codFilme = int(input("Informe o código do filme: "))
                        filmeSelect = filmes[codFilme]
                        dispCompra = filmeSelect[4]

                    print(f"Séria selecionada: {filmeSelect[1]}")

                else:
                    print("Nenhum filme cadastrado ainda!")
                    print("Retorno no menu anterior e cadastre um filme")

            elif opTipo == 3:  # Compra de Documentários
                if tamanhoDocumentario > 0:
                    print("< Compra de Documentários />")

                    print(f"Documentários: {documentarios}")
                    codDocumentario = int(
                        input("Informe o código do documentário: "))
                    documentariosSelect = documentarios[codDocumentario]
                    while codDocumentario < 0:
                        print("Opção inválda!! \n Vamos tentar novamente!")
                        print(f"Documentários: {documentarios}")
                        codDocumentario = int(
                            input("Informe o código do documentário: "))
                        documentariosSelect = documentarios[codDocumentario]

                    dispCompra = documentariosSelect[4]

                    while dispCompra == "Disponibilidade de Venda: False":
                        print(
                            "Opção não disponível para venda, vamos tentar novamente")
                        print(f"Documentários: {documentarios}")
                        codDocumentario = int(
                            input("Informe o código do documentário: "))
                        documentariosSelect = documentarios[codDocumentario]
                        dispCompra = documentariosSelect[4]

                    print(f"Séria selecionada: {documentariosSelect[1]}")

                else:
                    print("Nenhum documentário cadastrada ainda!")
                    print("Retorno no menu anterior e cadastre um documentário")

    elif opTarefa == 7:  # Tarefa 7 Cadastro de Clientes
        print("< Cadastro de Clientes />")

        codigoCliente += 1
        nomeCliente = input("Nome Cliente: ")

        cliente = cadastroCliente(codigoCliente, nomeCliente)
        clientes += [cliente]
        print("Cliente cadastrado com sucesso!")

    elif opTarefa == 8:  # Tarefa 8 Sair do NerdFlix
        print("Saindo do NerdFlix")
        break

    else:
        print("Opção inválda!! \n Vamos tentar novamente!")

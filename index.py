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
codCompra = 0

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


def cadastroCompra(codCompra, codCliente, nomeCliente, nomeProduto, preco):
    codCompra -= 1
    compras = []

    dataCompra = dataAtual()

    compras.insert(0, f"Código: {codCompra}")
    compras.insert(1, f"Código Cliente: {codCliente}")
    compras.insert(2, f"Nome: {nomeCliente}")
    compras.insert(3, f"Produto: {nomeProduto}")
    compras.insert(4, f"Preço: {preco}")
    compras.insert(5, f"Data da Compra: {dataCompra}")

    return compras


def Tipos():
    print("|1 - Série| |2 - Filme| |3 - Documentário|")
    print("Digite o número")


def TiposPlus():
    print("|1 - Série| |2 - Filme| |3 - Documentário| |4 - Clientes| |5 - Compras|")
    print("Digite o número")


def TiposRelatorio():
    print("|0 - Todos os Produtos| |1 - Filmes| |2 - Séries| |3 - Documentários| |4 - Disponíveis para Venda| |5 - Indiponível para Venda|")
    print("Digite o número")


def Tarefa():
    print("|1 - Cadastro| |2 - Consulta| |3 - Atualizar| |4 - Relatório| |5 - Registro de Compra| |6 - Relatório de Compra| |7 - Registro de Clientes| |8 - Sair|")
    print("Digite o número")


def Informacoes():
    print("|1 - Nome| |3 - Preço| |4 - Diponibilidade para Venda|")
    print("Digite o número")

# Inicio do Codigo


print("Bem Vindo (a) ao NerdFlix")

while True:

    tamanhoSeries = len(series)
    tamanhoFilmes = len(filmes)
    tamanhoDocumentarios = len(documentarios)
    tamanhoClientes = len(clientes)
    tamanhoCompras = len(compras)

    print("Escolha uma opção")
    Tarefa()
    opTarefa = int(input("Escolha uma opção acima: "))
    while opTarefa <= 0 or opTarefa >= 9:
        print("Opção inválida!! \n Vamos tentar novamente!")
        Tarefa()
        opTarefa = int(input("Escolha uma opção acima: "))

    if opTarefa == 1:  # Tarefa 1 Cadastro

        print("< Cadastro de Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0 or opTipo >= 4:
            print("Opção inválida!! \n Vamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Cadastro de Séries
            print("< Cadastro de Séries />")

            print("Iformações do Produto \n")
            codSerie += 1
            nome = input("Nome: ")
            tipo = 1
            preco = float(input("Preço: "))
            print("Informe True para disponível")
            print("Informe False para indisponível")
            venda = input("Disponibilidade para venda: ")
            if venda == "true":
                venda = "True"
            elif venda == "false":
                venda = "False"

            while venda != "True" and venda != "False":
                print("\nOpção inválida!! \nVamos tentar novamente!\n")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")

            serie = cadastro(codSerie, nome, tipo, preco, venda)
            series += [serie]
            print("Série cadastrada com sucesso!")

        elif opTipo == 2:  # Cadastro de Filmes
            print("< Cadastro de Filmes />")

            print("Iformações do Produto \n")
            codFilme += 1
            nome = input("Nome: ")
            tipo = 2
            preco = float(input("Preço: "))
            print("Informe True para disponível")
            print("Informe False para indisponível")
            venda = input("Disponibilidade para venda: ")
            if venda == "true":
                venda = "True"
            elif venda == "false":
                venda = "False"

            while venda != "True" and venda != "False":
                print("Opção inválida!! \nVamos tentar novamente!")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")

            filme = cadastro(codFilme, nome, tipo, preco, venda)
            filmes += [filme]
            print("Filme cadastrado com sucesso!")

        elif opTipo == 3:  # Cadastro de Documentários
            print("< Cadastro de Documentários />")

            print("Iformações do Produto \n")
            codDocumentario += 1
            nome = input("Nome: ")
            tipo = 3
            preco = float(input("Preço: "))
            print("Informe True para disponível")
            print("Informe False para indisponível")
            venda = input("Disponibilidade para venda: ")
            if venda == "true":
                venda = "True"
            elif venda == "false":
                venda = "False"

            while venda != "True" and venda != "False":
                print("Opção inválida!! \nVamos tentar novamente!")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")

            documentario = cadastro(codDocumentario, nome, tipo, preco, venda)
            documentarios += [documentario]
            print("Documentário cadastrado com sucesso!")

    elif opTarefa == 2:  # Tarefa 2 Consulta

        print("< Consulta de Produtos />")

        TiposPlus()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0 or opTipo >= 6:
            print("\nOpção inválida!!\nVamos tentar novamente!")
            TiposPlus()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Consulta de Série
            if tamanhoSeries <= 0:
                print("\nNenhuma série cadastrada!")
                print("Volte para o menu principal e cadastre uma série \n")
            else:
                print("Séries cadastradas:")
                print(series)

        elif opTipo == 2:  # Consulta de Filmes
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte para o menu principal e cadastre um filme \n")
            else:
                print("Filmes cadastrados:")
                print(filmes)

        elif opTipo == 3:  # Consulta de Documentários
            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte para o menu principal e cadastre um documentário \n")
            else:
                print("Documentário cadastrados:")
                print(documentarios)

        elif opTipo == 4:  # Consulta de Clientes
            if tamanhoClientes <= 0:
                print("\nNenhum cliente cadastrado!")
                print("Volte para o menu principal e cadastre um cliente \n")
            else:
                print("Clientes cadastrados:")
                print(clientes)

        elif opTipo == 5:  # Consulta de Compras
            if tamanhoCompras <= 0:
                print("\nNenhuma venda realizada!")
                print("Volte para o menu principal e realize uma venda \n")
            else:
                print("Compras cadastrados:")
                print(compras)

        else:
            print("Produto não cadastrado")

    elif opTarefa == 3:  # Tarefa 3 Atualizar

        print("< Atualizar Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0 or opTipo >= 4:
            print("\nOpção inválida!!\nVamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Atualizar Série
            if tamanhoSeries <= 0:
                print("\nNenhuma série cadastrada!")
                print("Volte para o menu principal e cadastre uma série \n")
            else:
                print("Lista de séries cadastradas:")
                print(series)

                codSerie = int(input("Informe o código: "))
                while codSerie < 0 or codSerie > tamanhoSeries:
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de séries cadastradas:")
                    print(series)
                    codSerie = int(input("Escolha uma opção acima: "))

                serieSelect = series[codSerie]

                print(f"Série informada {serieSelect[1]}")

                print("Selecione o que iremos alterar")
                Informacoes()

                codInfo = int(input("Escolha uma opção acima: "))
                while codInfo < 0 or codInfo >= 5:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                info = ""

                if codInfo == 1:
                    info = "Nome"
                elif codInfo == 3:
                    info = "Preço"
                elif codInfo == 4:
                    info = "Disponibilidade para Venda"
                else:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                if codInfo == 4:
                    date = input(f"Informe {info}: ")
                    if date == "Disponibilidade para Venda: true":
                        date = "Disponibilidade para Venda: True"
                    elif date == "Disponibilidade para Venda: false":
                        date = "Disponibilidade para Venda: False"

                    while date != "Disponibilidade para Venda: True" and date != "Disponibilidade para Venda: False":
                        print("Opção inválida!! \nVamos tentar novamente!")
                        print("Informe True para disponível")
                        print("Informe False para indisponível")
                        date = input(f"Informe {info}: ")
                date = input(f"Informe {info}: ")

                serieSelect[codInfo] = date

                print("Dado alterado com sucesso! \n")

        elif opTipo == 2:  # Atualizar Filme
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte para o menu principal e cadastre um filme \n")
            else:
                print("Lista de filmes cadastrados:")
                print(filmes)

                codFilme = int(input("Informe o código: "))
                while codFilme < 0 or codFilme > tamanhoFilmes:
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de fimes cadastrados:")
                    print(filmes)
                    codFilme = int(input("Escolha uma opção acima: "))

                filmeSelect = filmes[codFilme]

                print(f"Filme informado {filmeSelect[1]}")

                print("Selecione o que iremos alterar")
                Informacoes()

                codInfo = int(input("Escolha uma opção acima: "))
                while codInfo < 0 or codInfo >= 5:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                info = ""

                if codInfo == 1:
                    info = "Nome"
                elif codInfo == 3:
                    info = "Preço"
                elif codInfo == 4:
                    info = "Disponibilidade para Venda"
                else:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                if codInfo == 4:
                    date = input(f"Informe {info}: ")
                    print(f"Teste: {serieSelect[codInfo]}")

                    if date == "Disponibilidade para Venda: true":
                        date = "Disponibilidade para Venda: True"
                    elif date == "Disponibilidade para Venda: false":
                        date = "Disponibilidade para Venda: False"

                    while date != "Disponibilidade para Venda: True" and date != "Disponibilidade para Venda: False":
                        print("Opção inválida!! \nVamos tentar novamente!")
                        print("Informe True para disponível")
                        print("Informe False para indisponível")
                        date = input(f"Informe {info}: ")
                date = input(f"Informe {info}: ")

                serieSelect[codInfo] = date

                print("Dado alterado com sucesso! \n")

        elif opTipo == 3:  # Atualizar Documentário
            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte para o menu principal e cadastre um documentário \n")
            else:
                print("Lista de documentários cadastrados:")
                print(documentarios)

                codDocumentario = int(input("Informe o código: "))
                while codDocumentario < 0 or codDocumentario > tamanhoDocumentarios:
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de documentários cadastrados:")
                    print(documentarios)
                    codDocumentario = int(input("Escolha uma opção acima: "))

                documentarioSelect = documentarios[codDocumentario]

                print(f"Filme informado {documentarioSelect[1]}")

                print("Selecione o que iremos alterar")
                Informacoes()

                codInfo = int(input("Escolha uma opção acima: "))
                while codInfo < 0 or codInfo >= 5:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                info = ""

                if codInfo == 1:
                    info = "Nome"
                elif codInfo == 3:
                    info = "Preço"
                elif codInfo == 4:
                    info = "Disponibilidade para Venda"
                else:
                    print("\nOpção inválda!!\nVamos tentar novamente!")
                    Informacoes()
                    codInfo = int(input("Escolha uma opção acima: "))

                if codInfo == 4:
                    date = input(f"Informe {info}: ")
                    print(f"Teste: {serieSelect[codInfo]}")

                    if date == "Disponibilidade para Venda: true":
                        date = "Disponibilidade para Venda: True"
                    elif date == "Disponibilidade para Venda: false":
                        date = "Disponibilidade para Venda: False"

                    while date != "Disponibilidade para Venda: True" and date != "Disponibilidade para Venda: False":
                        print("Opção inválida!! \nVamos tentar novamente!")
                        print("Informe True para disponível")
                        print("Informe False para indisponível")
                        date = input(f"Informe {info}: ")
                date = input(f"Informe {info}: ")

                serieSelect[codInfo] = date

                print("Dado alterado com sucesso! \n")

    elif opTarefa == 4:  # Tarefa 4 Relatório
        print("< Relatório />")

        TiposRelatorio()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo < 0 or opTipo >= 6:
            print("\nOpção Inválida!\nVamos tentar novamente!")
            TiposRelatorio()
            opTipo = int(input("Escolha uma opção acima:"))

        if opTipo == 0:  # Todos os Produtos
            print("Todos os Produtos")
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte no menu anterior e cadastro um filme\n")
            else:
                print(f"Filmes: {filmes}")

            if tamanhoSeries <= 0:
                print("\nNenhuma série cadastrada!")
                print("Volte no menu anterior e cadastre uma série\n")
            else:
                print(f"Séries: {series}")

            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte no menu anterior e cadastro um documentário\n")
            else:
                print(f"Documentários: {documentarios}")

        elif opTipo == 1:  # Todos os Filmes
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte no menu anterior e cadastro um filme\n")
            else:
                print("Todos o filmes")
                print(f"Filmes: {filmes}")

        elif opTipo == 2:  # Todas as Séries
            if tamanhoSeries <= 0:
                print("\nNenhuma sérue cadastrada!")
                print("Volte no menu anterior e cadastro uma série\n")
            else:
                print("Todos o séries")
                print(f"Séries: {series}")

        elif opTipo == 3:  # Todos os Documentários
            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte no menu anterior e cadastro um documentário\n")
            else:
                print("Todos o documentários")
                print(f"Documentários: {documentarios}")

        elif opTipo == 4:  # Todos Diponíveis
            todosProdutos = series + filmes + documentarios
            totalProdutos = len(todosProdutos)

            if totalProdutos <= 0:
                print("Nenhum produto cadastrado!!")
                print("Volte no menu principal e cadastre um produto!")
            else:
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

            if totalProdutos <= 0:
                print("Nenhum produto cadastrado!!")
                print("Volte no menu principal e cadastre um produto!")
            else:
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

        if tamanhoClientes == 0:
            print("Nenhum cliente cadastrado ainda!")
            print("Acesso a opção 7 do menu anterior")
            print("Saindo...")
        else:
            print("Informe um cliente")
            print("Clientes cadastrados: ")
            print(clientes)

            codCliente = int(input("Informe o código: "))

            while codCliente < 0 or codCliente > tamanhoClientes:
                print("Opção inválda!! \n Vamos tentar novamente!")
                print("Clientes cadastrados: ")
                print(clientes)
                codCliente = int(input("Escolha uma opção acima: "))

            clienteSelect = clientes[codCliente]
            nomeCliente = clienteSelect[1]
            codCliente = clienteSelect[0]
            print(f"Cliente selecionado: {clienteSelect[1]}")

            print("Selecione o item para a compra: ")

            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))
            while opTipo <= 0 or opTipo >= 5:
                print("\nOpção inválda!!\nVamos tentar novamente!")
                Tipos()
                opTipo = int(input("Escolha uma opção acima: "))

            if opTipo == 1:  # Compra de Séries
                if tamanhoSeries <= 0:
                    print("Nenhuma série cadastrada ainda!")
                    print("Retorno no menu anterior e cadastre uma série")
                else:
                    print("< Compra de Séries />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        while True:
                            codCompra += 1
                            print(f"Séries: {series}")
                            codSerie = int(
                                input("Informe o código da série: "))
                            serieSelect = series[codSerie]
                            nomeProduto = serieSelect[1]
                            while codSerie < 0 or codSerie > tamanhoSeries:
                                print("\nOpção inválda!!\n Vamos tentar novamente!")
                                print(f"Séries: {series}")
                                codSerie = int(
                                    input("Informe o código da série: "))
                                serieSelect = series[codSerie]

                            dispCompra = serieSelect[4]

                            while dispCompra == "Disponibilidade de Venda: False":
                                print(
                                    "Opção não disponível para venda, vamos tentar novamente")
                                print(f"Séries: {series}")
                                codSerie = int(
                                    input("Informe o código da série: "))
                                serieSelect = series[codSerie]
                                dispCompra = serieSelect[4]

                            print("\nConfirma o nome da série para a venda?")
                            print(f"Séria selecionada: {serieSelect[1]}\n")
                            print("Informe -1 para confirmar")
                            print("Informe 0 ou outro número para alterar")
                            verificandoCompra = int(
                                input("Escolha opção acima: "))

                            if verificandoCompra == -1:
                                compra = cadastroCompra(
                                    codCompra, codCliente, nomeCliente, nomeProduto, preco)
                                compras += [compra]
                                print("Venda registrada com Sucesso!")
                                break

                            else:
                                confirmadoPedido = 0

                        print("Realizar mais uma venda?")
                        print("Digite -1 para finalizar")
                        print("Digite 0 para realizar uma nova venda")
                        condicaoVenda = int(input("Escolha uma opção acima: "))

                        if condicaoVenda == 0:
                            confirmadoPedido = 0
                        else:
                            confirmadoCompra = -1
                            print("Venda registrada com Sucesso!")

            elif opTipo == 2:  # Compra de Filmes
                if tamanhoFilmes <= 0:
                    print("Nenhum filme cadastrado ainda!")
                    print("Retorno no menu anterior e cadastre um filme")
                else:
                    print("< Compra de Filmes />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        while True:
                            codCompra += 1
                            print(f"Filmes: {filmes}")
                            codFilme = int(
                                input("Informe o código do filme: "))
                            filmeSelect = filmes[codFilme]
                            nomeProduto = filmeSelect[1]
                            while codFilme < 0 or codFilme > tamanhoFilmes:
                                print("Opção inválda!! \n Vamos tentar novamente!")
                                print(f"Filmes: {filmes}")
                                codFilme = int(
                                    input("Informe o código do filme: "))
                                filmeSelect = filmes[codFilme]

                            dispCompra = filmeSelect[4]

                            while dispCompra == "Disponibilidade de Venda: False":
                                print(
                                    "Opção não disponível para venda, vamos tentar novamente")
                                print(f"Filmes: {filmes}")
                                codFilme = int(
                                    input("Informe o código do filme: "))
                                filmeSelect = filmes[codFilme]
                                dispCompra = filmeSelect[4]

                            print("\nConfirma o nome do filme para a venda?")
                            print(f"Filme selecionado: {filmeSelect[1]}\n")
                            print("Informe -1 para confirmar")
                            print("Informe 0 ou outro número para alterar")
                            verificandoCompra = int(
                                input("Escolha opção acima: "))

                            if verificandoCompra == -1:
                                compra = cadastroCompra(
                                    codCompra, codCliente, nomeCliente, nomeProduto, preco)
                                compras += [compra]
                                print("Venda registrada com Sucesso!")
                                break

                            else:
                                confirmadoPedido = 0

                        print("Realizar mais uma venda?")
                        print("Digite -1 para finalizar")
                        print("Digite 0 para realizar uma nova venda")
                        condicaoVenda = int(input("Escolha uma opção acima: "))

                        if condicaoVenda == 0:
                            confirmadoPedido = 0
                        else:
                            confirmadoCompra = -1
                            print("Venda registrada com Sucesso!")

            elif opTipo == 3:  # Compra de Documentários
                if tamanhoDocumentarios <= 0:
                    print("Nenhum documentário cadastrado ainda!")
                    print("Retorno no menu anterior e cadastre um documentário")
                else:
                    print("< Compra de Documentário />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        while True:
                            codCompra += 1
                            print(f"Documentários: {documentarios}")
                            codDocumentario = int(
                                input("Informe o código do documentário: "))
                            documentarioSelect = documentarios[codDocumentario]
                            nomeProduto = documentarioSelect[1]
                            while codDocumentario < 0 or codDocumentario > tamanhoDocumentarios:
                                print("Opção inválda!! \n Vamos tentar novamente!")
                                print(f"Documentários: {documentarios}")
                                codDocumentario = int(
                                    input("Informe o código do documentário: "))
                                documentarioSelect = documentarios[codDocumentario]

                            dispCompra = documentarioSelect[4]

                            while dispCompra == "Disponibilidade de Venda: False":
                                print(
                                    "Opção não disponível para venda, vamos tentar novamente")
                                print(f"Documentários: {documentarios}")
                                codDocumentario = int(
                                    input("Informe o código do documentário: "))
                                documentarioSelect = documentarios[codDocumentario]
                                dispCompra = documentarioSelect[4]

                            print("\nConfirma o nome do documentário para a venda?")
                            print(
                                f"Filme selecionado: {documentarioSelect[1]}\n")
                            print("Informe -1 para confirmar")
                            print("Informe 0 ou outro número para alterar")
                            verificandoCompra = int(
                                input("Escolha opção acima: "))

                            if verificandoCompra == -1:
                                compra = cadastroCompra(
                                    codCompra, codCliente, nomeCliente, nomeProduto, preco)
                                compras += [compra]
                                print("Venda registrada com Sucesso!")
                                break

                            else:
                                confirmadoPedido = 0

                        print("Realizar mais uma venda?")
                        print("Digite -1 para finalizar")
                        print("Digite 0 para realizar uma nova venda")
                        condicaoVenda = int(input("Escolha uma opção acima: "))

                        if condicaoVenda == 0:
                            confirmadoPedido = 0
                        else:
                            confirmadoCompra = -1
                            print("Venda registrada com Sucesso!")

    elif opTarefa == 6:  # Tarefa 6 Relatório de Compra
        print("< Relatório de Compra />")

        if tamanhoClientes <= 0:
            print("Nenhum cliente cadastrado ainda!")
            print("Acesse a opção 7 do menu anterior")
            print("Saindo...")

        elif tamanhoCompras <= 0:
            print("Nenhuma compra cadastrado ainda!")
            print("Acesse a opção 5 do menu anterior")
            print("Saindo...")

        else:
            print("Informe um cliente")
            print("Clientes cadastrados: ")
            print(clientes)

            codCliente = int(input("Informe o código: "))
            while codCliente < 0 or codCliente > tamanhoClientes:
                print("\nOpção inválda!!\n Vamos tentar novamente!")
                Informacoes()
                codCliente = int(input("Escolha uma opção acima: "))

            clienteSelect = clientes[codCliente]
            nomeCliente = clienteSelect[1]
            print(f"Cliente selecionado: {clienteSelect[1]}")

            comprasCliente = []

            for i in range(tamanhoCompras):
                compra = compras

                print(f"COMPRA AQUI: {compra[1]}")
                print(f"CODIGO DO CLIENTE AQUI: {codCliente}")

                if compra == f"Código Cliente: Código: {codCliente}":
                    comprasCliente += compras[i]

            print(f"{compras}")

    elif opTarefa == 7:  # Tarefa 7 Cadastro de Clientes
        print("< Cadastro de Clientes />")

        codigoCliente += 1
        nomeCliente = input("Nome Cliente: ")

        cliente = cadastroCliente(codigoCliente, nomeCliente)
        clientes += [cliente]
        print("\nCliente cadastrado com sucesso!\n")

    elif opTarefa == 8:  # Tarefa 8 Sair do NerdFlix

        print("Saindo do NerdFlix")
        break

    else:
        print("\nOpção inválda!!\n Vamos tentar novamente!")

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
    # Funcao Para pegar data atual
    hoje = datetime.date.today()
    return hoje


def cadastro(codigo, nome, tipo, preco, venda):
    # Funcao para cadastro dos produtos em sua lista correta (Filmes, Series e Documentários)
    codigo -= 1
    produtos = []

    produtos.insert(0, f"Código: {codigo}")
    produtos.insert(1, f"Nome: {nome}")
    produtos.insert(2, f"Tipo: {tipo}")
    produtos.insert(3, f"Preço: {preco}")
    produtos.insert(4, f"Disponibilidade de Venda: {venda}")

    return produtos


def cadastroCliente(codigoCliente, nomeCliente):
    # Funcao para cadastro dos clientes
    codigoCliente -= 1
    clientes = []

    clientes.insert(0, f"Código: {codigoCliente}")
    clientes.insert(1, f"Nome Cliente: {nomeCliente}")

    return clientes


def cadastroCompra(codCompra, codCliente, nomeCliente, nomeProduto, preco):
    # Funcao para cadastro das vendas
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
    # Funcao somente para printar os tipos dos produtos
    print("|1 - Série| |2 - Filme| |3 - Documentário|")
    print("Digite o número")


def TiposPlus():
    # Funcao somente para printar os tipos dos produtos + clientes e compras
    print("|1 - Série| |2 - Filme| |3 - Documentário| |4 - Clientes| |5 - Compras|")
    print("Digite o número")


def TiposRelatorio():
    # Funcao somente para printar os tipos do relatórios
    print("|0 - Todos os Produtos| |1 - Filmes| |2 - Séries| |3 - Documentários| |4 - Disponíveis para Venda| |5 - Indiponível para Venda|")
    print("Digite o número")


def Tarefa():
    # Funcao somente para printar as tarefas que o sistema realiza
    print("|1 - Cadastro| |2 - Consulta| |3 - Atualizar| |4 - Relatório| |5 - Registro de Compra| |6 - Relatório de Compra| |7 - Registro de Clientes| |8 - Sair|")
    print("Digite o número")


def Informacoes():
    # Funcao somente para printar as informacoes do produto
    print("|1 - Nome| |3 - Preço| |4 - Diponibilidade para Venda|")
    print("Digite o número")


def tabelaProdutos(tamanhoProduto, tipoProduto):
    # Funcao para criar e printar as tabelas dos produtos
    print("|Código| |Nome| |Tipo| |Preço| |Diposnibilidade de Venda|")

    for i in range(tamanhoProduto):
        tipoProdutoSelect = tipoProduto[i]

        codProdutoSelect = tipoProdutoSelect[0]
        nomeProdutoSelect = tipoProdutoSelect[1]
        precoProdutoSelect = tipoProdutoSelect[2]
        dispVendaSelect = tipoProdutoSelect[3]

        print(
            f"|{codProdutoSelect} {nomeProdutoSelect} {precoProdutoSelect} {dispVendaSelect}|")


def tabelaClientes():
    # Funcao para criar e printar a tabela dos clientes
    print("\nClientes cadastrados")
    print("|Código| |Nome|")

    for i in range(tamanhoClientes):
        clienteSelect = clientes[i]

        codCliente = clienteSelect[0]
        nomeCliente = clienteSelect[1]

        print(
            f"|{codCliente} {nomeCliente}|")


# Inicio do Codigo
print("Bem Vindo (a) ao NerdFlix")

while True:

    # Declaracao das variaveis com os tamanhos dos produtos, clientes e compras
    tamanhoSeries = len(series)
    tamanhoFilmes = len(filmes)
    tamanhoDocumentarios = len(documentarios)
    tamanhoClientes = len(clientes)
    tamanhoCompras = len(compras)
    todosProdutos = series + filmes + documentarios
    tamanhoProdutos = len(todosProdutos)

    print("\nEscolha uma opção")
    Tarefa()
    opTarefa = int(input("Escolha uma opção acima: "))
    while opTarefa <= 0 or opTarefa >= 9:
        # While que verifica a entrada do usuário
        print("Opção inválida!!\nVamos tentar novamente!")
        Tarefa()
        opTarefa = int(input("Escolha uma opção acima: "))

    if opTarefa == 1:  # Tarefa 1 Cadastro

        print("\n< Cadastro de Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        erro = 0
        while opTipo <= 0 or opTipo >= 4:
            # While que verifica a entrada do usuário
            print("Opção inválida!!\nVamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))
            erro += 1

            while erro >= 3:
                # While da sacanagem
                print("Oh animal! Digite um número correto!")
                print("Agora só de sacanagem vai ficar preso aqui!")
                i = input("Digite 1 sair: ")

                while True:
                    print("")
                    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAAH")

        if opTipo == 1:  # Cadastro de Séries
            print("\n< Cadastro de Séries />")

            print("Iformações do Produto")
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
                # While que verifica a entrada do usuário
                print("\nOpção inválida!!\nVamos tentar novamente!")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")
                if venda == "true":
                    venda = "True"
                elif venda == "false":
                    venda = "False"

            serie = cadastro(codSerie, nome, tipo, preco, venda)
            series += [serie]
            print("\nSérie cadastrada com sucesso!")

        elif opTipo == 2:  # Cadastro de Filmes
            print("\n< Cadastro de Filmes />")

            print("Iformações do Produto")
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
                # While que verifica a entrada do usuário
                print("\nOpção inválida!!\nVamos tentar novamente!")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")
                if venda == "true":
                    venda = "True"
                elif venda == "false":
                    venda = "False"

            filme = cadastro(codFilme, nome, tipo, preco, venda)
            filmes += [filme]
            print("\nFilme cadastrado com sucesso!")

        elif opTipo == 3:  # Cadastro de Documentários
            print("\n< Cadastro de Documentários />")

            print("Iformações do Produto")
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
                # While que verifica a entrada do usuário
                print("\nOpção inválida!!\nVamos tentar novamente!")
                print("Informe True para disponível")
                print("Informe False para indisponível")
                venda = input("Disponibilidade para venda: ")
                if venda == "true":
                    venda = "True"
                elif venda == "false":
                    venda = "False"

            documentario = cadastro(codDocumentario, nome, tipo, preco, venda)
            documentarios += [documentario]
            print("\nDocumentário cadastrado com sucesso!")

    elif opTarefa == 2:  # Tarefa 2 Consulta

        print("\n< Consulta de Produtos />")

        TiposPlus()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0 or opTipo >= 6:
            # While que verifica a entrada do usuário
            print("\nOpção inválida!!\nVamos tentar novamente!")
            TiposPlus()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Consulta de Série
            if tamanhoSeries <= 0:
                # Verifica se tem série cadastrada
                print("\nNenhuma série cadastrada!")
                print("Volte para o menu principal e cadastre uma série \n")
            else:
                print("\nSéries Cadastradas")

                tamanhoProduto = tamanhoSeries
                tipoProduto = series
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 2:  # Consulta de Filmes
            if tamanhoFilmes <= 0:
                # Verifica se tem filme cadastrado
                print("\nNenhum filme cadastrado!")
                print("Volte para o menu principal e cadastre um filme \n")
            else:
                print("\nFilmes Cadastrados")

                tamanhoProduto = tamanhoFilmes
                tipoProduto = filmes
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 3:  # Consulta de Documentários
            if tamanhoDocumentarios <= 0:
                # Verifica se tem documentário cadastrado
                print("\nNenhum documentário cadastrado!")
                print("Volte para o menu principal e cadastre um documentário \n")
            else:
                print("\nDocumentários Cadastrados")

                tamanhoProduto = tamanhoDocumentarios
                tipoProduto = documentarios
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 4:  # Consulta de Clientes
            if tamanhoClientes <= 0:
                # Verifica se tem cliente cadastrado
                print("\nNenhum cliente cadastrado!")
                print("Volte para o menu principal e cadastre um cliente \n")
            else:
                tabelaClientes()

        elif opTipo == 5:  # Consulta de Compras
            if tamanhoCompras <= 0:
                # Verifica se tem compras cadastradas
                print("\nNenhuma venda realizada!")
                print("Volte para o menu principal e realize uma venda \n")
            else:
                print("\nCompras cadastrados:")
                print(compras)

        else:
            print("Produto não cadastrado")

    elif opTarefa == 3:  # Tarefa 3 Atualizar

        print("\n< Atualizar Produtos />")

        Tipos()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo <= 0 or opTipo >= 4:
            # While que verifica a entrada do usuário
            print("\nOpção inválida!!\nVamos tentar novamente!")
            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))

        if opTipo == 1:  # Atualizar Série
            if tamanhoSeries <= 0:
                print("\nNenhuma série cadastrada!")
                print("Volte para o menu principal e cadastre uma série \n")
            else:
                print("\nLista de séries cadastradas")

                tamanhoProduto = tamanhoSeries
                tipoProduto = series
                tabelaProdutos(tamanhoProduto, tipoProduto)

                codSerie = int(input("Informe o código: "))
                while codSerie < 0 or codSerie >= tamanhoSeries:
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de séries cadastradas\n")

                    tamanhoProduto = tamanhoSeries
                    tipoProduto = series
                    tabelaProdutos(tamanhoProduto, tipoProduto)

                    codSerie = int(input("Escolha uma opção acima: "))

                serieSelect = series[codSerie]

                print(f"\nSérie informada {serieSelect[1]}\n")

                print("\nSelecione o que iremos alterar")
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

                print("\nDado alterado com sucesso!\n")

        elif opTipo == 2:  # Atualizar Filme
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte para o menu principal e cadastre um filme \n")
            else:
                print("\nLista de filmes cadastrados")

                tamanhoProduto = tamanhoFilmes
                tipoProduto = filmes
                tabelaProdutos(tamanhoProduto, tipoProduto)

                codFilme = int(input("Informe o código: "))
                while codFilme < 0 or codFilme >= tamanhoFilmes:
                    # While que verifica a entrada do usuário
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de fimes cadastrados\n")

                    tamanhoProduto = tamanhoFilmes
                    tipoProduto = filmes
                    tabelaProdutos(tamanhoProduto, tipoProduto)

                    codFilme = int(input("Escolha uma opção acima: "))

                filmeSelect = filmes[codFilme]

                print(f"\nFilme informado {filmeSelect[1]}\n")

                print("\nSelecione o que iremos alterar")
                Informacoes()

                codInfo = int(input("Escolha uma opção acima: "))
                while codInfo < 0 or codInfo >= 5:
                    # While que verifica a entrada do usuário
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
                        # While que verifica a entrada do usuário
                        print("Opção inválida!! \nVamos tentar novamente!")
                        print("Informe True para disponível")
                        print("Informe False para indisponível")
                        date = input(f"Informe {info}: ")
                date = input(f"Informe {info}: ")

                serieSelect[codInfo] = date

                print("\nDado alterado com sucesso!\n")

        elif opTipo == 3:  # Atualizar Documentário
            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte para o menu principal e cadastre um documentário \n")
            else:
                print("\nLista de documentários cadastrados")

                tamanhoProduto = tamanhoDocumentarios
                tipoProduto = documentarios
                tabelaProdutos(tamanhoProduto, tipoProduto)

                codDocumentario = int(input("Informe o código: "))
                while codDocumentario < 0 or codDocumentario >= tamanhoDocumentarios:
                    # While que verifica a entrada do usuário
                    print("\nOpção inválida!!\nVamos tentar novamente!")
                    print("Lista de documentários cadastrados\n")

                    tamanhoProduto = tamanhoDocumentarios
                    tipoProduto = documentarios
                    tabelaProdutos(tamanhoProduto, tipoProduto)

                    codDocumentario = int(input("Escolha uma opção acima: "))

                documentarioSelect = documentarios[codDocumentario]

                print(f"\nDocumentário informado {documentarioSelect[1]}\n")

                print("\nSelecione o que iremos alterar")
                Informacoes()

                codInfo = int(input("Escolha uma opção acima: "))
                while codInfo < 0 or codInfo >= 5:
                    # While que verifica a entrada do usuário
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
                        # While que verifica a entrada do usuário
                        print("Opção inválida!! \nVamos tentar novamente!")
                        print("Informe True para disponível")
                        print("Informe False para indisponível")
                        date = input(f"Informe {info}: ")
                date = input(f"Informe {info}: ")

                serieSelect[codInfo] = date

                print("\nDado alterado com sucesso! \n")

    elif opTarefa == 4:  # Tarefa 4 Relatório
        print("\n< Relatório />")

        TiposRelatorio()
        opTipo = int(input("Escolha uma opção acima: "))
        while opTipo < 0 or opTipo >= 6:
            # While que verifica a entrada do usuário
            print("\nOpção Inválida!\nVamos tentar novamente!")
            TiposRelatorio()
            opTipo = int(input("Escolha uma opção acima:"))

        if opTipo == 0:  # Todos os Produtos
            if tamanhoProdutos <= 0:
                print("\nNenhum produto cadastrado ainda!")
                print("Volte no menu anterior e cadastre um produto")
            else:
                print("\nTodos os Produtos")
                tamanhoProduto = tamanhoProdutos
                tipoProduto = todosProdutos
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 1:  # Todos os Filmes
            if tamanhoFilmes <= 0:
                print("\nNenhum filme cadastrado!")
                print("Volte no menu anterior e cadastro um filme\n")
            else:
                print("\nTodos os filmes")

                tamanhoProduto = tamanhoFilmes
                tipoProduto = filmes
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 2:  # Todas as Séries
            if tamanhoSeries <= 0:
                print("\nNenhuma série cadastrada!")
                print("Volte no menu anterior e cadastro uma série\n")
            else:
                print("\nTodos as séries")

                tamanhoProduto = tamanhoSeries
                tipoProduto = series
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 3:  # Todos os Documentários
            if tamanhoDocumentarios <= 0:
                print("\nNenhum documentário cadastrado!")
                print("Volte no menu anterior e cadastro um documentário\n")
            else:
                print("\nTodos os documentários")

                tamanhoProduto = tamanhoDocumentarios
                tipoProduto = documentarios
                tabelaProdutos(tamanhoProduto, tipoProduto)

        elif opTipo == 4:  # Todos Diponíveis
            todosProdutos = series + filmes + documentarios
            totalProdutos = len(todosProdutos)

            if totalProdutos <= 0:
                print("Nenhum produto cadastrado!!")
                print("Volte no menu principal e cadastre um produto!")
            else:
                true = []
                for i in range(totalProdutos):
                    produtoSelect = todosProdutos[i]
                    teste = produtoSelect[4]
                    if teste == 'Disponibilidade de Venda: True':
                        true += [produtoSelect]

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
        print("\n< Registro de Compras />")

        if tamanhoClientes == 0:
            print("\nNenhum cliente cadastrado ainda!")
            print("Acesso a opção 7 do menu anterior")
            print("Saindo...")
        else:
            print("Informe um cliente")

            tabelaClientes()

            codCliente = int(input("Informe o código: "))

            while codCliente < 0 or codCliente >= tamanhoClientes:
                # While que verifica a entrada do usuário
                print("\nOpção inválda!!\nVamos tentar novamente!")

                tabelaClientes()
                codCliente = int(input("Escolha uma opção acima: "))

            clienteSelect = clientes[codCliente]
            nomeCliente = clienteSelect[1]
            codCliente = clienteSelect[0]
            print(f"\nCliente selecionado: {clienteSelect[1]}\n")

            print("\nSelecione o item para a compra: ")

            Tipos()
            opTipo = int(input("Escolha uma opção acima: "))
            while opTipo <= 0 or opTipo > 3:
                # While que verifica a entrada do usuário
                print("\nOpção inválda!!\nVamos tentar novamente!")
                Tipos()
                opTipo = int(input("Escolha uma opção acima: "))

            if opTipo == 1:  # Compra de Séries
                if tamanhoSeries <= 0:
                    print("\nNenhuma série cadastrada ainda!")
                    print("Retorno no menu anterior e cadastre uma série")
                else:
                    print("\n< Compra de Séries />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        tamanhoProduto = tamanhoSeries
                        tipoProduto = series

                        while True:
                            codCompra += 1
                            tabelaProdutos(tamanhoProduto, tipoProduto)

                            codSerie = int(
                                input("Informe o código da série: "))
                            serieSelect = series[codSerie]
                            nomeProduto = serieSelect[1]
                            while codSerie < 0 or codSerie >= tamanhoSeries:
                                print("\nOpção inválda!!\n Vamos tentar novamente!")

                                tabelaProdutos(tamanhoProduto, tipoProduto)

                                codSerie = int(
                                    input("Informe o código da série: "))
                                serieSelect = series[codSerie]

                            dispCompra = serieSelect[4]
                            # Verifica se o produto está cadastrado, se nao, nao deixa dar sequencia
                            while dispCompra == "Disponibilidade de Venda: False":
                                if tamanhoSeries == 1:
                                    print("Produto indiponível para venda...")
                                    print(
                                        "Consultamos e não temos nenhum produto para venda, volte no menu anterios e cadastre um produto disponível para venda!!")
                                    print("Saindo...")
                                    break
                                else:
                                    tabelaProdutos(tamanhoProduto, tipoProduto)
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
                                print("\nVenda registrada com Sucesso!")
                                break

                            else:
                                confirmadoPedido = 0

                        print("Realizar mais uma venda?")
                        print("Digite -1 para finalizar")
                        print("Digite 0 para realizar uma nova venda")
                        condicaoVenda = int(input("Escolha uma opção acima: "))

                        if condicaoVenda <= 0:
                            confirmadoPedido = 0
                        else:
                            confirmadoCompra = -1
                            print("\nVenda registrada com Sucesso!")

            elif opTipo == 2:  # Compra de Filmes
                if tamanhoFilmes <= 0:
                    print("\nNenhum filme cadastrado ainda!")
                    print("Retorno no menu anterior e cadastre um filme")
                else:
                    print("\n< Compra de Filmes />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        tamanhoProduto = tamanhoFilmes
                        tipoProduto = filmes

                        while True:
                            codCompra += 1
                            tabelaProdutos(tamanhoProduto, tipoProduto)
                            codFilme = int(
                                input("Informe o código do filme: "))
                            filmeSelect = filmes[codFilme]
                            nomeProduto = filmeSelect[1]
                            while codFilme < 0 or codFilme > tamanhoFilmes:
                                print("\nOpção inválda!!\nVamos tentar novamente!")

                                tabelaProdutos(tamanhoProduto, tipoProduto)
                                codFilme = int(
                                    input("Informe o código do filme: "))
                                filmeSelect = filmes[codFilme]

                            dispCompra = filmeSelect[4]

                            while dispCompra == "Disponibilidade de Venda: False":
                                if tamanhoFilmes == 1:
                                    print("Produto indiponível para venda...")
                                    print(
                                        "Consultamos e não temos nenhum produto para venda, volte no menu anterios e cadastre um produto disponível para venda!!")
                                    print("Saindo...")
                                else:
                                    tabelaProdutos(tamanhoProduto, tipoProduto)
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
                                print("\nVenda registrada com Sucesso!")
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
                            print("\nVenda registrada com Sucesso!")

            elif opTipo == 3:  # Compra de Documentários
                if tamanhoDocumentarios <= 0:
                    print("\nNenhum documentário cadastrado ainda!")
                    print("Retorno no menu anterior e cadastre um documentário")
                else:
                    print("\n< Compra de Documentário />")

                    confirmadoCompra = 0
                    confirmadoPedido = 0

                    while confirmadoCompra != -1:
                        tamanhoProduto = tamanhoDocumentarios
                        tipoProduto = documentarios

                        while True:
                            codCompra += 1

                            tabelaProdutos(tamanhoProduto, tipoProduto)
                            codDocumentario = int(
                                input("Informe o código do documentário: "))
                            documentarioSelect = documentarios[codDocumentario]
                            nomeProduto = documentarioSelect[1]
                            while codDocumentario < 0 or codDocumentario >= tamanhoDocumentarios:
                                print("Opção inválda!!\nVamos tentar novamente!")

                                tabelaProdutos(tamanhoProduto, tipoProduto)
                                codDocumentario = int(
                                    input("Informe o código do documentário: "))
                                documentarioSelect = documentarios[codDocumentario]

                            dispCompra = documentarioSelect[4]

                            while dispCompra == "Disponibilidade de Venda: False":

                                if tamanhoDocumentarios == 1:
                                    print("Produto indiponível para venda...")
                                    print(
                                        "Consultamos e não temos nenhum produto para venda, volte no menu anterios e cadastre um produto disponível para venda!!")
                                    print("Saindo...")
                                    break
                                else:
                                    tabelaProdutos(tamanhoProduto, tipoProduto)
                                    codDocumentario = int(
                                        input("Informe o código do documentário: "))
                                    documentarioSelect = documentarios[codDocumentario]
                                    dispCompra = documentarioSelect[4]

                            print("\nConfirma o nome do documentário para a venda?")
                            print(f"Filme selecionado: {documentarioSelect[1]}\n")
                            print("Informe -1 para confirmar")
                            print("Informe 0 ou outro número para alterar")
                            verificandoCompra = int(
                                input("Escolha opção acima: "))

                            if verificandoCompra == -1:
                                compra = cadastroCompra(
                                    codCompra, codCliente, nomeCliente, nomeProduto, preco)
                                compras += [compra]
                                print("\nVenda registrada com Sucesso!")
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
                            print("\nVenda registrada com Sucesso!")

    elif opTarefa == 6:  # Tarefa 6 Relatório de Compra
        print("\n< Relatório de Compra />")

        if tamanhoClientes <= 0:
            # Verifica sem tem clientes cadastrados
            print("Nenhum cliente cadastrado ainda!")
            print("Acesse a opção 7 do menu anterior")
            print("Saindo...")

        elif tamanhoCompras <= 0:
            # Verifica sem tem compras cadastradas
            print("Nenhuma compra cadastrado ainda!")
            print("Acesse a opção 5 do menu anterior")
            print("Saindo...")

        else:
            print("Informe um cliente")

            tabelaClientes()

            codCliente = int(input("Informe o código: "))
            while codCliente < 0 or codCliente >= tamanhoClientes:
                # While que verifica a entrada do usuário
                print("\nOpção inválda!!\n Vamos tentar novamente!")
                tabelaClientes()
                codCliente = int(input("Escolha uma opção acima: "))

            clienteSelect = clientes[codCliente]
            nomeCliente = clienteSelect[1]
            print(f"\nCliente selecionado: {clienteSelect[1]}\n")

            comprasCliente = []

            for i in range(tamanhoCompras):
                compraSelect = compras[i]
                codCompra = compraSelect[0]

                if codCompra == f"Código: {codCliente}":
                    comprasCliente += [compraSelect]

            print(f"{comprasCliente}")

    elif opTarefa == 7:  # Tarefa 7 Cadastro de Clientes
        print("\n< Cadastro de Clientes />")

        codigoCliente += 1
        nomeCliente = input("Nome Cliente: ")

        cliente = cadastroCliente(codigoCliente, nomeCliente)
        clientes += [cliente]
        print("\nCliente cadastrado com sucesso!")

    elif opTarefa == 8:  # Tarefa 8 Sair do NerdFlix

        print("Saindo do NerdFlix")
        break

    else:
        print("\nOpção inválda!!\n Vamos tentar novamente!")

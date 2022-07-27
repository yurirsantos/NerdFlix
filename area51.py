print("< Relatório de Compra />")
codigos = [0, 1, 2]
nomes = ["Suits", "Top Gun", "TBL"]
precos = [199, 200, 200]
total = 0

tamanhoCodigos = len(codigos)

print("Código - Nome - Tipo - Preço")

for i in range(tamanhoCodigos):

    # Pegar um código
    codigo = codigos[i]
    # Pegar um nome
    nome = nomes[i]
    # Pegar um preco
    preco = precos[i]

    # Prints dos itens
    print(f"{codigo}    {nome}    {preco}")

    # Pegar valor total
    precoSelect = precos[i]
    total += precoSelect


print(f"Valor total: {total}")

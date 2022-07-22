# NerdFlix

# Trabalho Final Algoritmos

## Sistema NerdFlix

Você foi contratado(a) para trabalhar na startup NerdFlix, uma empresa que disponibiliza produtos (filmes, séries e documentários) por meio de stream. A empresa possui um sistema Web onde o cliente se cadastra, adquire produtos e realiza pagamentos.
Você foi incumbido de administrar os dados no backoffice da empresa, isto é, num sistema interno. Como ainda não cursou a disciplina de BD na UFFS, você ainda não sabe como integrar os dados entre os dois sistemas. Desta forma, você decidiu criar outro sistema em Python onde os funcionários da NerdFlix irão digitar novamente todas as compras realizadas pelos pelos clientes no sistema Web.
Nas próximas seções são descritas as informações necessárias para a implementação do sistema.

## Objetivo

O objetivo de seu programa é possibilitar que o usuário (funcionário da empresa) cadastre os produtos e também registre as compras feitas pelos clientes.
Neste momento, o sistema não terá um cadastro de clientes completo. Assim, cada compra será vinculada apenas ao login do cliente.
Abaixo, são detalhadas as opções que devem estar presentes no menu principal:

## 1 - Cadastrar produtos

O usuário do sistema poderá criar um novo produto informando os seguintes dados cadastrais:

<ul> 

<li> <strong> Código do produto </strong>: código numérico do produto; </li>
<li> <strong> Nome </strong>: nome do produto; </li>
<li> <strong> Tipo </strong>: 1 para série, 2 para filme, 3 para documentário; </li>
<li> <strong> Preço </strong>: valor de venda do produto;  </li>
<li> <strong> Disponível para venda </strong>: valor booleano que indica se o produto pode (True) ou não (False) ser vendido neste momento. </li>

</ul>

## 2 - Consultar produto

Permite buscar os dados de um determinado produto pelo seu código. Caso o produto não exista, exibir a mensagem <strong> Produto não cadastrado </strong>.

## 3 - Atualizar produtos

Permite que dados de um determinado produto sejam atualizados. Como o código identifica um produto, este não pode ser alterado.

## 4 - Relatório de produtos

Ao acessar esta opção, o sistema deve perguntar o que o usuário de seja visualizar: todos os produtos (opção 0), somente filmes (opção 1), séries (opção 2), documentários (opção 3), todos os produtos disponíveis para venda (opção 4) ou todos os produtos indisponíveis (opção 5).
Em seguida, exibir a lista de produtos, filtrados conforme opção descrita acima. Devem ser exibidas as colunas código, nome, tipo e preço. A lista deve vir ordenada pelo nome do produto. O tipo deve ser exibido com sua descrição textual (embora armazenado na forma de número).

<ul> 
<li> DICA: você pode adicionar um conjunto de 10 produtos predefinidos diretamente no código-fonte, a fim de facilitar os testes da aplicação. </li>
</ul>

## 5 - Registrar compra

Para registrar uma compra, primeiramente é necessário informar o login do cliente (string). O sistema também deve gerar automaticamente a data da compra e armazená-la. Em seguida, deve ser informado o código de cada produto (após a digitação, deverá ser apresentado o nome do produto para que o usuário se certifique de que digitou o código correto). Se for informado o código de um produto não disponível para venda, o sistema deve reportar um erro e impedir a inserção do mesmo no registro da compra. Deverá existir uma forma de encerrar o registro da compra (dica: pode ser o código -1 , por exemplo). A forma de pagamento não será controlada. Ao final, o sistema deverá apresentar um tipo de cupom fiscal. Ex.:

![image](https://user-images.githubusercontent.com/91801482/180485702-08bbbc55-26a2-4a4b-8e53-a259c0cf803c.png)

## 6 - Relatório de compras

Mostrar uma lista com todas as compras, contendo: data (dd/mm/aaaa), login do cliente e valor total.

# Avaliação

1 - Execução correta e boa explicação: 80%

<ul>
<li> Serão feitos vários testes durante a apresentação. </li
</ul>

2 - Estilo de programação: 10%

<ul>
<li> Código <strong> comentado </strong> (sem excesso), bem estruturado, nomes de variáveis significativas, etc. </li
<li> Devem ser utilizadas <strong> funções </strong> </li
</ul>

3 - Funções adicionais para melhorar a funcionalidade básica da aplicação: 10%

<ul>
<li> Por exemplo: utilizar o conceito de estrutura (class); implementar o cadastro dos clientes, etc. </li
</ul>

## Trabalhos iguais irão resultar em nota igual à zero para todos os envolvidos

# Exemplo de código

![image](https://user-images.githubusercontent.com/91801482/180486237-049149d2-c803-4b4b-9b48-d2d400b9d60a.png)

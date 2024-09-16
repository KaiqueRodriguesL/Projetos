# Lista para armazenar os produtos
produtos = []

def cadastrar_produto():
    print("Cadastro de Produto")
    nome = input("Nome do Produto: ")
    descricao = input("Descrição do Produto: ")
    valor = float(input("Valor do Produto: "))
    disponivel = input("Disponível para venda (sim/não): ").lower() == 'sim'
    dataCompra = input("Data de Compra (EX: 01/01/1999) ")
    
    produtos.append({
        'nome': nome,
        'descricao': descricao,
        'valor': valor,
        'disponivel': disponivel,
        'data de compra': dataCompra

    })
    
    print("Produto cadastrado com sucesso!\n")

def listar_produtos():
    print("Listagem de Produtos")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        produtos_ordenados = sorted(produtos, key=lambda x: x['dataCompra'])
        for produto in produtos_ordenados:
            print(f"Nome: {produto['nome']}, Valor: R$ {produto['valor']}, Data de Compra: {produto['dataCompra']}")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar novo produto")
        print("2 - Listar produtos por valor")
        print("3 - Sair")
        opcao = input("Opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
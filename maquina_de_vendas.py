# Sistema Completo de Máquina de Vendas

produtos = {
    1: {"nome": "Coca Cola 2L", "preco": 10.99, "estoque": 10},
    2: {"nome": "Sal Lebre", "preco": 5.99, "estoque": 10},
    3: {"nome": "Arroz Tio João 1kg", "preco": 7.50, "estoque": 10},
    4: {"nome": "Feijão Urbano 1kg", "preco": 8.90, "estoque": 10},
}

carrinho = []
total = 0.0

# Menu de seleção de produtos
while True:
    print("\n=== PRODUTOS DISPONÍVEIS ===")
    for codigo, item in produtos.items():
        status = "ESGOTADO" if item['estoque'] == 0 else f"R${item['preco']}"
        print(f"{codigo} - {item['nome']} - {status} (Estoque: {item['estoque']})")
    print("0 - Finalizar compra e ir para pagamento")

    try:
        id = int(input("Digite o ID do produto: "))
    except (ValueError, OSError):
        print("Entrada inválida.")
        continue

    if id == 0:
        break

    if id not in produtos:
        print("Código inválido!")
        continue

    produto = produtos[id]
    if produto['estoque'] == 0:
        print("Produto esgotado!")
        continue

    try:
        quantidade = int(input(f"Digite a quantidade de {produto['nome']}: "))
    except (ValueError, OSError):
        print("Quantidade inválida.")
        continue

    if quantidade <= 0:
        print("Quantidade inválida!")
        continue

    if quantidade > produto['estoque']:
        print("Quantidade maior que o estoque disponível!")
        continue

    produto['estoque'] -= quantidade
    subtotal = quantidade * produto['preco']
    total += subtotal
    carrinho.append((produto['nome'], quantidade, subtotal))
    print(f"Adicionado ao carrinho: {quantidade}x {produto['nome']} - R${subtotal:.2f}")

# Exibir resumo da compra
print("\n=== RESUMO DA COMPRA ===")
for nome, qtd, sub in carrinho:
    print(f"{qtd}x {nome} - R${sub:.2f}")
print(f"Total a pagar: R${total:.2f}")

# Opções de pagamento
print("\n=== FORMAS DE PAGAMENTO ===")
print("1 - Crédito")
print("2 - Débito")
print("3 - Pix")
print("4 - Espécie")

while True:
    try:
        pagamento = int(input("Escolha a forma de pagamento: "))
    except (ValueError, OSError):
        print("Digite um número válido.")
        continue

    if pagamento == 1:
        try:
            parcelar = int(input("Deseja parcelar? (1 = sim / 0 = não): "))
        except (ValueError, OSError):
            parcelar = 0

        if parcelar == 1:
            print("1 - Parcelar em 2x")
            print("2 - Parcelar em 3x")
            while True:
                try:
                    escolha = int(input("Escolha (1 ou 2): "))
                    if escolha == 1:
                        print(f"Compra parcelada em 2x de R${total/2:.2f}")
                        break
                    elif escolha == 2:
                        print(f"Compra parcelada em 3x de R${total/3:.2f}")
                        break
                    else:
                        print("Opção inválida!")
                except (ValueError, OSError):
                    print("Entrada inválida!")
        else:
            print(f"Total a pagar no crédito: R${total:.2f}")
        break

    elif pagamento == 2:
        print(f"Débito selecionado. Total a pagar: R${total:.2f}")
        break

    elif pagamento == 3:
        print(f"Pix selecionado. Total a pagar: R${total:.2f}")
        print("Chave Pix: pagamento@maquina.com")
        break

    elif pagamento == 4:
        print(f"Espécie selecionada. Total a pagar: R${total:.2f}")
        break

    else:
        print("Forma de pagamento inválida. Tente novamente.")

# Simular pagamento: entrada manual do valor pago
while True:
    try:
        valor_pago = float(input("Digite o valor inserido na máquina: R$ "))
        if valor_pago < total:
            print(f"Valor insuficiente. Faltam R${total - valor_pago:.2f}")
            continue
        break
    except (ValueError, OSError):
        print("Valor inválido. Tente novamente.")

troco = valor_pago - total
print(f"Troco: R${troco:.2f}")
print("\n=== COMPRA FINALIZADA ===")
print("Obrigado por comprar na nossa máquina de vendas!")
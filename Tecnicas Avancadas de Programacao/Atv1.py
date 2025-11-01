# -----------------------------
# Classe Produto
# -----------------------------
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_info(self):
        return f"{self.nome} | R$ {self.preco:.2f} | Estoque: {self.estoque}"

    def vender(self, quantidade):
        # Reduz estoque se disponível
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            total = quantidade * self.preco
            return total
        else:
            return None  # estoque insuficiente

    def repor(self, quantidade):
        self.estoque += quantidade

# -----------------------------
# Classe Loja
# -----------------------------
class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print(f"Produtos disponíveis na {self.nome}:")
        for produto in self.produtos:
            print(" -", produto.exibir_info())

    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                return produto
        return None

# -----------------------------
# Classe Cliente
# -----------------------------
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.carrinho.append((produto, quantidade))
            print(f"{quantidade} x {produto.nome} adicionado ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}.")

    def finalizar_compra(self, loja, forma_pagamento, desconto=0):
        print("\nRecibo de Compra")
        print(f"Cliente: {self.nome}")
        print(f"Loja: {loja.nome}")
        print(f"Forma de Pagamento: {forma_pagamento}\n")

        subtotal = 0
        for produto, quantidade in self.carrinho:
            valor = produto.vender(quantidade)
            if valor is not None:
                print(f"{quantidade} x {produto.nome} → R$ {valor:.2f}")
                subtotal += valor
            else:
                print(f"Não foi possível comprar {produto.nome} (estoque insuficiente).")

        # Aplicando desconto
        if forma_pagamento == 'Débito':
          desconto = 0.1
        elif forma_pagamento == 'Crédito':
          desconto = 0.05
        elif forma_pagamento == 'Pix':
          desconto = 0.1
        else:
          desconto = 0

        # Finalizando a venda
        valor_desconto = subtotal * desconto
        print(f"\n Desconto aplicado: {desconto*100:.0f}% ({forma_pagamento})→ -R$ {valor_desconto:.2f}")

        total_final = subtotal - valor_desconto
        print("\n Total a pagar: R$ {:.2f}".format(total_final))
        self.carrinho.clear()
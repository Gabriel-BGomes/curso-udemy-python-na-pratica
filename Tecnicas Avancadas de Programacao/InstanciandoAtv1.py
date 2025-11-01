# Criando os Produtos
from Atv1 import Produto
from Atv1 import Loja
from Atv1 import Cliente

p1 = Produto("Notebook Dell", 3500.00, 5)
p2 = Produto("Mouse Sem Fio", 120.00, 20)
p3 = Produto("Teclado Mecânico", 450.00, 10)

p4 = Produto("TV 32", 999.00, 20)
p5 = Produto("Monitor 22", 699.00, 30)
p6 = Produto("Bolsa Para Notebook", 199.00, 40)

# Criando as Lojas
loja1 = Loja("Tech Store")
loja1.adicionar_produto(p1)
loja1.adicionar_produto(p2)
loja1.adicionar_produto(p3)

loja2 = Loja("Multi Shop")
loja2.adicionar_produto(p1)
loja2.adicionar_produto(p4)
loja2.adicionar_produto(p5)
loja2.adicionar_produto(p6)

# Criando os Cliente
cliente1 = Cliente("Ana Silva")
cliente2 = Cliente("Marcos Araujo")
cliente3 = Cliente("Gabriela Aguiar")

# Cliente adiciona produtos ao carrinho
cliente1.adicionar_ao_carrinho(p1, 1)   # 1 notebook
cliente1.adicionar_ao_carrinho(p2, 2)   # 2 mouses
cliente1.adicionar_ao_carrinho(p3, 1)   # 1 teclado mecânico

cliente2.adicionar_ao_carrinho(p1, 1)   # 1 notebook
cliente2.adicionar_ao_carrinho(p6, 1)   # 1 Bolsa Para Notebook

cliente3.adicionar_ao_carrinho(p1, 1)   # 1 notebook
cliente3.adicionar_ao_carrinho(p3, 1)   # 1 teclado mecânico

# Finalizando compra com Pix e 10% de desconto
cliente1.finalizar_compra(loja1, forma_pagamento="Pix", desconto=0.10)

cliente1.finalizar_compra(loja1, forma_pagamento="Débito", desconto=0.10)
cliente2.finalizar_compra(loja2, forma_pagamento="Crédito", desconto=0.15)
cliente3.finalizar_compra(loja1, forma_pagamento="Pix", desconto=0.10)

# Conferindo estoque atualizado
print("\n Estoque atualizado após a compra:")
loja1.listar_produtos()
loja2.listar_produtos()
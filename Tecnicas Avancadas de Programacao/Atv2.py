# ---------------------
# Classe Funcionário
# ---------------------
class Funcionario:
  def __init__(self, nome, cargo, salbruto):
    self.nome = nome
    self.cargo = cargo
    self.salbruto = salbruto
    self.beneficios = []

  def adicionar_beneficio(self, valor):
    self.beneficios.append(valor)

  def total_beneficios(self):
    return sum(self.beneficios)

# ----------------------------
# Cálculo do INSS
# ----------------------------
  def calcular_inss(self):
    if self.salbruto <= 1518.00:
      aliquota, parcela = 0.075, 0.00
    elif self.salbruto <= 2793.88:
      aliquota, parcela = 0.09, 22.77
    elif self.salbruto <= 4190.83:
      aliquota, parcela = 0.12, 106.59
    elif self.salbruto <= 8157.41:
      aliquota, parcela = 0.14, 190.40
    else:
      aliquota, parcela = 0.14, 190.40

    desconto_inss = self.salbruto * aliquota - parcela
    return desconto_inss

# ----------------------------
# Cálculo do IRRF
# ----------------------------
  def calcular_irrf(self):
    base = self.salbruto - self.calcular_inss()
    if base <= 2259.21:
      return 0.0
    elif base <= 2826.65:
      aliquota, parcela = 0.075, 169.44
    elif base <= 3751.05:
      aliquota, parcela = 0.15, 381.44
    elif base <= 4664.68:
      aliquota, parcela = 0.225, 662.77
    else:
      aliquota, parcela = 0.275, 896.00

    desconto_irrf = base * aliquota - parcela
    return desconto_irrf

# ----------------------------
# Salário líquido
# ----------------------------
  def salario_liquido(self):
    liquido = self.salbruto - self.calcular_inss() - self.calcular_irrf() - self.total_beneficios()
    return liquido

# ----------------------------
# Total de descontos
# ----------------------------
  def total_descontos(self):
    return self.calcular_inss() + self.calcular_irrf() + self.total_beneficios()


# ---------------------
# Classe Empresa
# ---------------------
class Empresa:
  def __init__(self, nome):
    self.nome = nome
    self.funcionarios = []

  def adicionar_funcionario(self, funcionario):
    self.funcionarios.append(funcionario)

  def folha_pagamento(self):
    print(f"\n--- Folha de Pagamento - {self.nome} ---\n")
    for f in self.funcionarios:
      print(f"Nome: {f.nome}")
      print(f"Cargo: {f.cargo}")
      print(f"Salário Bruto: R$ {f.salbruto:.2f}")
      print(f"Total Benefícios: R$ {f.total_beneficios():.2f}")
      print(f"INSS: R$ {f.calcular_inss():.2f}")
      print(f"IRRF: R$ {f.calcular_irrf():.2f}")
      print(f"Total Descontos: R$ {f.total_descontos():.2f}")
      print(f"Salário Líquido: R$ {f.salario_liquido():.2f}")
      print("-" * 40)
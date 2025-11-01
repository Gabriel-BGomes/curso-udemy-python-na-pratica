from Atv2 import Empresa
from Atv2 import Funcionario

# --------------------
# Instanciando
# --------------------
empresa = Empresa("Associação de tecnologia ADT")

f1 = Funcionario("João", "Analista", 3500)
f1.adicionar_beneficio(200) #VT
f1.adicionar_beneficio(220) #VR

f2 = Funcionario("Maria", "Desenvolvedora", 4000)
f2.adicionar_beneficio(220) #VT
f2.adicionar_beneficio(300) #VR

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)

empresa.folha_pagamento()
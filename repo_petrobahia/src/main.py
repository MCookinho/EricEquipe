import ast
from services.pedido_service import processar_pedido
from services.clientes_service import cadastrar_cliente

pedidos = [
    {"cliente": "TransLog", "produto": "diesel", "qtd": 1200, "cupom": "MEGA10"},
    {"cliente": "MoveMais", "produto": "gasolina", "qtd": 300, "cupom": None},
    {"cliente": "EcoFrota", "produto": "etanol", "qtd": 50, "cupom": "NOVO5"},
    {"cliente": "PetroPark", "produto": "lubrificante", "qtd": 12, "cupom": "LUB2"},
]

clientes = []
with open("../data/clientes.txt", "r", encoding="utf-8") as f:
    for linha in f:
        if linha.strip():
            clientes.append(ast.literal_eval(linha.strip()))

print("==== Início processamento PetroBahia ====")

for c in clientes:
    ok = cadastrar_cliente(c)
    if ok:
        print("cliente ok:", c["nome"])
    else:
        print("cliente com problema:", c)

valores = []
for p in pedidos:
    v = processar_pedido(p)
    valores.append(v)
    print("pedido:", p, "-- valor final:", v)

print("TOTAL =", sum(valores))
print("==== Fim processamento PetroBahia ====")

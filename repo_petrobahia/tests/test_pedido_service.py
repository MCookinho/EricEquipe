from src.services.pedido_service import PedidoService

def test_pedido_qtd_zero():
    svc = PedidoService()
    p = {"cliente": "X", "produto": "etanol", "qtd": 0, "cupom": None}
    assert svc.processar(p) == 0.0

def test_pedido_produto_desconhecido():
    svc = PedidoService()
    p = {"cliente": "X", "produto": "inexistente", "qtd": 5, "cupom": None}
    # comportamento esperado: retornar 0 ou valor zero-like
    v = svc.processar(p)
    assert isinstance(v, (int, float))
    assert v >= 0

def test_pedido_com_cupom_e_valor_positivo():
    svc = PedidoService()
    p = {"cliente": "Y", "produto": "diesel", "qtd": 1200, "cupom": "MEGA10"}
    v = svc.processar(p)
    assert isinstance(v, (int, float))
    assert v > 0

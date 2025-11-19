import pytest
from src.services.preco_service import PrecoService


def _get_calc_fn(service):
    # compatibilidade com nomes diferentes usados durante refactor
    return getattr(service, "calcular", getattr(service, "calcular_preco"))


def test_calcular_preco_basico():
    svc = PrecoService()
    calc = _get_calc_fn(svc)

    valor = calc("diesel", 100)
    assert isinstance(valor, (int, float))
    assert valor > 0

    # produto desconhecido deve retornar 0
    assert calc("produto_inexistente_xyz", 10) == 0

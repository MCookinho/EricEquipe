from typing import Dict

BASES: Dict[str, float] = {
    "diesel": 3.99,
    "gasolina": 5.19,
    "etanol": 3.59,
    "lubrificante": 25.0,
}


class PrecoService:
    """Serviço de cálculo de preços de produtos PetroBahia."""

    def __init__(self, bases: Dict[str, float] = None):
        self.bases = bases or BASES

    def calcular_preco(self, tipo: str, qtd: float) -> float:
        """Calcula o preço total para um tipo de produto e quantidade."""
        if tipo not in self.bases:
            print(f"[AVISO] Tipo de produto desconhecido: {tipo}")
            return 0.0

        metodo = getattr(self, f"_calc_{tipo}", None)
        if metodo is None:
            print(f"[ERRO] Nenhum cálculo definido para tipo '{tipo}'")
            return 0.0

        preco = metodo(qtd)
        return round(preco, 2)

    # --- Cálculos específicos por tipo ---

    def _calc_diesel(self, qtd: float) -> float:
        base = self.bases["diesel"]
        preco = base * qtd

        if qtd > 1000:
            preco *= 0.9
        elif qtd > 500:
            preco *= 0.95

        return preco

    def _calc_gasolina(self, qtd: float) -> float:
        base = self.bases["gasolina"]
        preco = base * qtd
        if qtd > 200:
            preco -= 100
        return preco

    def _calc_etanol(self, qtd: float) -> float:
        base = self.bases["etanol"]
        preco = base * qtd
        if qtd > 80:
            preco *= 0.97
        return preco

    def _calc_lubrificante(self, qtd: int) -> float:
        base = self.bases["lubrificante"]
        return base * qtd



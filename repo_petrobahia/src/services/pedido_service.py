from services.preco_service import PrecoService
from utils.log_config import setup_logger


class PedidoService:
    """Processa pedidos aplicando cálculo de preços."""

    def __init__(self):
        self.logger = setup_logger("pedido_service")
        self.preco_service = PrecoService()

    def processar(self, pedido: dict) -> float:
        """Processa o pedido e calcula o valor final."""

        self.logger.info("Processando pedido: %s", pedido)

        cliente = pedido.get("cliente", "desconhecido")
        produto = pedido.get("produto")
        qtd = pedido.get("qtd", 0)
        cupom = pedido.get("cupom")

        if not produto:
            self.logger.error("Pedido inválido (sem produto): %s", pedido)
            return 0.0

        if qtd <= 0:
            self.logger.warning("Pedido de %s com quantidade inválida: %s", cliente, qtd)
            return 0.0

        preco = self.preco_service.calcular_preco(produto, qtd, cupom)

        if produto == "diesel":
            preco = round(preco, 0)
        elif produto == "gasolina":
            preco = round(preco, 2)
        else:
            preco = float(int(preco * 100) / 100)

        self.logger.info(
            "Pedido concluído: Cliente=%s, Produto=%s, Qtd=%s, Valor Final=R$ %.2f",
            cliente, produto, qtd, preco
        )

        return preco

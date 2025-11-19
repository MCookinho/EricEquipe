from src.services.preco_service import PrecoService
from src.utils.log_config import setup_logger


class PedidoService:
    def __init__(self):
        self.logger = setup_logger("pedido_service")
        self.preco_service = PrecoService()

    def processar(self, pedido: dict) -> float:
        """
        Processa um pedido e calcula o preço final com base no produto, quantidade e cupom.
        """

        self.logger.info(f"Processando pedido: {pedido}")

        # Validação básica
        cliente = pedido.get("cliente", "desconhecido")
        produto = pedido.get("produto")
        qtd = pedido.get("qtd", 0)
        # cupom = pedido.get("cupom") # Variável não é usada

        if not produto:
            self.logger.error(f"Pedido inválido (sem produto): {pedido}")
            return 0.0

        if qtd <= 0:
            self.logger.warning(f"Pedido de {cliente} com quantidade inválida: {qtd}")
            return 0.0

        # O preco_service.calcular_preco não aceita 'cupom'
        preco = self.preco_service.calcular_preco(produto, qtd)

        # Pós-processamento de arredondamento
        if produto == "diesel":
            preco = round(preco, 0)
        elif produto == "gasolina":
            preco = round(preco, 2)
        else:
            preco = float(int(preco * 100) / 100.0)

        self.logger.info(
            f"Pedido concluído: Cliente={cliente}, Produto={produto}, "
            f"Qtd={qtd}, Valor Final=R$ {preco:.2f}"
        )

        return preco
    

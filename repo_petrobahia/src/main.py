from services.clientes_service import ClienteService
from services.pedido_service import PedidoService
from utils.log_config import setup_logger


def main():
    logger = setup_logger("main")

    logger.info("=== Iniciando sistema PetroBahia ===")

    cliente_service = ClienteService()
    pedido_service = PedidoService()

    # Exemplo de clientes
    clientes = [
        {"nome": "João Silva", "email": "joao.silva@petrobahia.com"},
        {"nome": "Maria Souza", "email": "maria.souza@@petrobahia.com"},  # inválido
    ]

    # Cadastra clientes
    for c in clientes:
        cliente_service.cadastrar(c)

    # Exemplo de pedidos
    pedidos = [
        {"cliente": "João Silva", "produto": "diesel", "qtd": 800, "cupom": "MEGA10"},
        {"cliente": "Maria Souza", "produto": "gasolina", "qtd": 150, "cupom": "NOVO5"},
        {"cliente": "João Silva", "produto": "lubrificante", "qtd": 3, "cupom": "LUB2"},
    ]

    for p in pedidos:
        try:
            preco = pedido_service.processar(p)
            logger.info(f"Pedido concluído: {p['cliente']} => R$ {preco:.2f}")
        except Exception as e:
            logger.exception(f"Erro ao processar pedido {p}: {e}")

    logger.info("=== Encerrando sistema PetroBahia ===")


if __name__ == "__main__":
    main()

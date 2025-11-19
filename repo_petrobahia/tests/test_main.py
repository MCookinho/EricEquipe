import pytest
from unittest.mock import patch, MagicMock

# Caminho do módulo principal
from src.main import main


@pytest.fixture
def mock_logger():
    """Mock de logger para capturar chamadas de log."""
    with patch("src.main.setup_logger") as mock_setup_logger:
        mock = MagicMock()
        mock_setup_logger.return_value = mock
        yield mock


@pytest.fixture
def mock_cliente_service():
    """Mock para ClienteService."""
    with patch("src.main.ClienteService") as mock_class:
        instance = MagicMock()
        mock_class.return_value = instance
        yield instance


@pytest.fixture
def mock_pedido_service():
    """Mock para PedidoService."""
    with patch("src.main.PedidoService") as mock_class:
        instance = MagicMock()
        # Processar retorna um preço fictício
        instance.processar.return_value = 100.0
        mock_class.return_value = instance
        yield instance


def test_main_flow(mock_logger, mock_cliente_service, mock_pedido_service):
    """Testa o fluxo principal da função main usando mocks."""

    main()

    # --- Verifica chamadas de log ---
    assert mock_logger.info.call_count >= 2
    mock_logger.info.assert_any_call("=== Iniciando sistema PetroBahia ===")
    mock_logger.info.assert_any_call("=== Encerrando sistema PetroBahia ===")

    # --- Verifica que os clientes foram cadastrados ---
    assert mock_cliente_service.cadastrar.call_count == 2
    mock_cliente_service.cadastrar.assert_any_call(
        {"nome": "João Silva", "email": "joao.silva@petrobahia.com"}
    )
    mock_cliente_service.cadastrar.assert_any_call(
        {"nome": "Maria Souza", "email": "maria.souza@petrobahia.com"}
    )

    # --- Verifica que os pedidos foram processados ---
    assert mock_pedido_service.processar.call_count == 3

    mock_pedido_service.processar.assert_any_call(
        {"cliente": "João Silva", "produto": "diesel", "qtd": 800, "cupom": "MEGA10"}
    )
    mock_pedido_service.processar.assert_any_call(
        {"cliente": "Maria Souza", "produto": "gasolina", "qtd": 150, "cupom": "NOVO5"}
    )

    # Para o lubrificante
    mock_pedido_service.processar.assert_any_call(
        {"cliente": "João Silva", "produto": "lubrificante", "qtd": 3, "cupom": "LUB2"}
    )

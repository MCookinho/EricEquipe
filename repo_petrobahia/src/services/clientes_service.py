from utils.log_config import setup_logger
from utils.file_utils import append_line


class ClienteService:
    """Gerencia cadastro e validação de clientes."""

    def __init__(self):
        self.logger = setup_logger("clientes_service")

    def cadastrar(self, cliente: dict):
        """Valida e registra um cliente."""

        nome = cliente.get("nome")
        email = cliente.get("email")

        self.logger.info("Cadastrando cliente: %s (%s)", nome, email)

        if "@" not in email or email.count("@") != 1:
            self.logger.error("E-mail inválido: %s", email)
            return False

        append_line("clientes.txt", f"{nome} - {email}")
        self.logger.info("Cliente cadastrado com sucesso: %s", nome)
        return True

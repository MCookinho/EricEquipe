import re
from pathlib import Path
from typing import Dict, Any
from src.utils import file_utils
from src.utils.log_config import setup_logger

REG_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
CLIENTES_PATH = Path("clientes.txt")


class ClienteService:
    """Serviço responsável por cadastrar e validar clientes PetroBahia."""

    def __init__(self, storage_path: Path = CLIENTES_PATH):
        self.storage_path = storage_path
        self.logger = setup_logger("clientes_service")

    def validar_cliente(self, cliente: Dict[str, Any]) -> bool:
        """Valida campos obrigatórios e formato de e-mail."""
        if "email" not in cliente or "nome" not in cliente:
            self.logger.error("Campos obrigatórios ausentes: 'email' e/ou 'nome'.")
            raise ValueError("Campos obrigatórios ausentes: 'email' e/ou 'nome'.")

        if not REG_EMAIL.match(cliente["email"]):
            self.logger.warning(f"E-mail inválido: {cliente['email']}")
            return False

        return True

    def salvar_cliente(self, cliente: Dict[str, Any]) -> None:
        """Salva cliente em arquivo."""
        file_utils.FileUtils.append_line(self.storage_path, cliente)

    def cadastrar(self, cliente: Dict[str, Any]) -> bool:
        """Fluxo completo de cadastro de cliente."""
        self.logger.info(f"Cadastrando cliente: {cliente.get('nome')} ({cliente.get('email')})")
        try:
            if not self.validar_cliente(cliente):
                return False
        except ValueError as e:
            return False

        self.salvar_cliente(cliente)
        self.enviar_email_boas_vindas(cliente["email"])
        return True

    def enviar_email_boas_vindas(self, email: str) -> None:
        """Simula o envio de e-mail de boas-vindas."""
        self.logger.info(f"Enviando e-mail de boas-vindas para {email}")

import re
from pathlib import Path
from typing import Dict, Any
from utils import file_utils

REG_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
CLIENTES_PATH = Path("clientes.txt")


class ClienteService:
    """Serviço responsável por cadastrar e validar clientes PetroBahia."""

    def __init__(self, storage_path: Path = CLIENTES_PATH):
        self.storage_path = storage_path

    def validar_cliente(self, cliente: Dict[str, Any]) -> bool:
        """Valida campos obrigatórios e formato de e-mail."""
        if "email" not in cliente or "nome" not in cliente:
            raise ValueError("Campos obrigatórios ausentes: 'email' e/ou 'nome'.")

        if not REG_EMAIL.match(cliente["email"]):
            print(f"[AVISO] E-mail inválido: {cliente['email']}")
            return False

        return True

    def salvar_cliente(self, cliente: Dict[str, Any]) -> None:
        """Salva cliente em arquivo."""
        file_utils.append_line(self.storage_path, cliente)

    def cadastrar(self, cliente: Dict[str, Any]) -> bool:
        """Fluxo completo de cadastro de cliente."""
        try:
            self.validar_cliente(cliente)
        except ValueError as e:
            print(f"[ERRO] {e}")
            return False

        self.salvar_cliente(cliente)
        self.enviar_email_boas_vindas(cliente["email"])
        return True

    def enviar_email_boas_vindas(self, email: str) -> None:
        """Simula o envio de e-mail de boas-vindas."""
        print(f"Enviando e-mail de boas-vindas para {email}")

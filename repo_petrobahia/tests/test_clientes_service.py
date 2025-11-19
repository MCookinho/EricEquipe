import os
from pathlib import Path
import pytest

from src.services.clientes_service import ClienteService

def test_cadastrar_cliente_valido(tmp_path, monkeypatch):
    svc = ClienteService()

    # Se a classe expõe storage_path, usamos tmp_path para não poluir repo
    if hasattr(svc, "storage_path"):
        svc.storage_path = tmp_path / "clientes.txt"
    else:
        # caso o serviço utilize utils.file_utils, criamos o arquivo alvo
        pass

    cliente = {"nome": "Teste Unit", "email": "teste@exemplo.com", "cnpj": "0001"}
    ok = svc.cadastrar(cliente)
    assert ok is True

    # Verifica se arquivo foi criado e contém algo (quando aplicável)
    path = getattr(svc, "storage_path", tmp_path / "clientes.txt")
    if path.exists():
        content = path.read_text(encoding="utf-8")
        assert "Teste Unit" in content or "teste@exemplo.com" in content

def test_cadastrar_cliente_invalido_sem_nome(tmp_path):
    svc = ClienteService()
    if hasattr(svc, "storage_path"):
        svc.storage_path = tmp_path / "clientes.txt"
    cliente = {"email": "semnome@exemplo.com"}
    ok = svc.cadastrar(cliente)
    assert ok is False

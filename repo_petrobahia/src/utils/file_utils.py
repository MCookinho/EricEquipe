from pathlib import Path
from typing import Any, List, Union


class FileUtils:
    """Classe utilitária para leitura e escrita simples em arquivos de texto."""

    @staticmethod
    def append_line(file_path: Union[str, Path], data: Any) -> None:
        """
        Adiciona uma linha (texto) ao final de um arquivo.
        Se o arquivo não existir, ele será criado.
        """
        path = Path(file_path)
        with path.open("a", encoding="utf-8") as f:
            f.write(str(data) + "\n")

    @staticmethod
    def read_lines(file_path: Union[str, Path]) -> List[str]:
        """
        Lê todas as linhas de um arquivo e retorna uma lista de strings.
        Retorna lista vazia se o arquivo não existir.
        """
        path = Path(file_path)
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    @staticmethod
    def overwrite(file_path: Union[str, Path], lines: List[Any]) -> None:
        """
        Sobrescreve completamente um arquivo com as linhas fornecidas.
        """
        path = Path(file_path)
        with path.open("w", encoding="utf-8") as f:
            for line in lines:
                f.write(str(line) + "\n")

    @staticmethod
    def delete(file_path: Union[str, Path]) -> None:
        """
        Remove o arquivo, se ele existir.
        """
        path = Path(file_path)
        if path.exists():
            path.unlink()
            

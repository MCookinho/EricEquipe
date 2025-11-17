import logging
from pathlib import Path

# Caminho padrão do log
LOG_PATH = Path("logs/app.log")
LOG_PATH.parent.mkdir(exist_ok=True)  # Cria a pasta logs/ se não existir


def setup_logger(name: str = "petrobahia", level: int = logging.INFO) -> logging.Logger:
    """
    Configura e retorna um logger formatado e pronto para uso.
    Pode ser usado por qualquer módulo do projeto.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Evita duplicação de handlers (import múltiplo)
    if logger.hasHandlers():
        return logger

    # --- Formato das mensagens ---
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # --- Console handler ---
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # --- File handler ---
    file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # --- Adiciona handlers ---
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


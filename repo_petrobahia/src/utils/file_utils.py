from pathlib import Path
from typing import Any, List, Union


def append_line(file_path: Union[str, Path], data: Any) -> None:
    path = Path(file_path)
    with path.open("a", encoding="utf-8") as f:
        f.write(str(data) + "\n")


def read_lines(file_path: Union[str, Path]) -> List[str]:
    path = Path(file_path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def overwrite(file_path: Union[str, Path], lines: List[Any]) -> None:
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(str(line) + "\n")


def delete(file_path: Union[str, Path]) -> None:
    path = Path(file_path)
    if path.exists():
        path.unlink()

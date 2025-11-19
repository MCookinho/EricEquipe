from pathlib import Path
from src.utils.file_utils import append_line, read_lines, overwrite, delete

def test_file_utils_append_read_overwrite_delete(tmp_path):
    path = tmp_path / "fu_test.txt"
    append_line(path, "linha1")
    append_line(path, "linha2")

    lines = read_lines(path)
    assert "linha1" in lines and "linha2" in lines

    overwrite(path, ["nova1", "nova2"])
    lines2 = read_lines(path)
    assert lines2 == ["nova1", "nova2"]

    delete(path)
    assert not path.exists()

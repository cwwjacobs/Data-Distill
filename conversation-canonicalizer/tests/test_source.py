"""Purpose: source-stage tests for determinism and explicit read status."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from engine.source.file_loader import load_file
from engine.source.source_registry import load_sources, register_sources


def test_load_file_success_reads_content(tmp_path: Path) -> None:
    source_path = tmp_path / "sample.txt"
    source_path.write_text("hello", encoding="utf-8")

    source_file = load_file(source_path)

    assert source_file.read_status == "ok"
    assert source_file.raw_content == "hello"
    assert source_file.read_error is None


def test_load_file_missing_reports_error(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.txt"

    source_file = load_file(missing_path)

    assert source_file.read_status == "error"
    assert source_file.raw_content is None
    assert source_file.read_error is not None


def test_register_sources_is_deterministic_and_ordered(tmp_path: Path) -> None:
    path_a = tmp_path / "a.txt"
    path_b = tmp_path / "b.txt"
    path_a.write_text("A", encoding="utf-8")
    path_b.write_text("B", encoding="utf-8")
    paths = [str(path_a), str(path_b)]

    first = register_sources(paths)
    second = register_sources(paths)

    assert [s.path for s in first] == [s.path for s in second]
    assert [s.source_id for s in first] == [s.source_id for s in second]
    assert first[0].path.endswith("a.txt")
    assert first[1].path.endswith("b.txt")


def test_load_sources_aliases_register_sources(tmp_path: Path) -> None:
    path_a = tmp_path / "one.txt"
    path_a.write_text("1", encoding="utf-8")
    paths = [str(path_a)]

    assert load_sources(paths) == register_sources(paths)

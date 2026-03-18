"""Purpose: deterministic local file loading for source stage."""

from hashlib import sha256
from pathlib import Path

from schemas.source_file import SourceFile


def _build_source_id(path: Path, raw_content: str | None, read_status: str, read_error: str | None) -> str:
    """Derive a deterministic source ID from path + read result."""
    digest_input = "|".join(
        [
            path.resolve().as_posix(),
            read_status,
            raw_content or "",
            read_error or "",
        ]
    )
    return sha256(digest_input.encode("utf-8")).hexdigest()


def load_file(path: Path) -> SourceFile:
    """Load a file and return explicit success/error status."""
    try:
        raw_content = path.read_text(encoding="utf-8")
        read_status = "ok"
        read_error = None
    except (FileNotFoundError, PermissionError, OSError) as exc:
        raw_content = None
        read_status = "error"
        read_error = f"{exc.__class__.__name__}: {exc}"

    source_id = _build_source_id(path=path, raw_content=raw_content, read_status=read_status, read_error=read_error)
    return SourceFile(
        source_id=source_id,
        path=path.resolve().as_posix(),
        read_status=read_status,
        raw_content=raw_content,
        read_error=read_error,
    )

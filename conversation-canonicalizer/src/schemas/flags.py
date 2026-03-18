"""Purpose: warning/ambiguity/loss flag schema contract."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class WarningFlag:
    """Warning/ambiguity/loss flag emitted by canonicalization."""

    type: Literal["warning", "ambiguity", "loss"]
    code: str
    message: str
    path: str | None
    severity: Literal["info", "warn", "error"]

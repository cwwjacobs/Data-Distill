"""Purpose: emit warning/ambiguity/loss flags explicitly."""

from __future__ import annotations

from schemas.flags import WarningFlag
from schemas.raw_record import RawRecord


def emit_flags(raw_record: RawRecord) -> list[WarningFlag]:
    """Emit deterministic Phase 1 ambiguity/loss flags from a raw record."""
    flags: list[WarningFlag] = []
    messages = raw_record.raw_payload.get("messages", [])

    for message_index, message in enumerate(messages):
        if not isinstance(message, dict):
            continue

        role = message.get("role")
        if not isinstance(role, str):
            flags.append(
                WarningFlag(
                    type="ambiguity",
                    code="AMBIGUOUS_ROLE_NON_STRING",
                    message="Message role is ambiguous or non-string; normalized to 'unknown'.",
                    path=f"messages[{message_index}].role",
                    severity="warn",
                )
            )

        if "blocks" in message:
            flags.append(
                WarningFlag(
                    type="loss",
                    code="LOSS_UNSUPPORTED_BLOCKS",
                    message="Message contains unsupported 'blocks'; lossy handling required downstream.",
                    path=f"messages[{message_index}].blocks",
                    severity="warn",
                )
            )

    return flags

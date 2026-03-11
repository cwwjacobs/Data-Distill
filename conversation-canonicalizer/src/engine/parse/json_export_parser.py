"""Purpose: parse one supported export JSON format."""

from __future__ import annotations

import json
from typing import Any


def _validate_message(message: Any, conv_idx: int, msg_idx: int) -> None:
    if not isinstance(message, dict):
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].messages[{msg_idx}] must be an object")
    if "role" not in message:
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].messages[{msg_idx}].role is required")
    if "content" not in message:
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].messages[{msg_idx}].content is required")


def _validate_conversation(conversation: Any, conv_idx: int) -> None:
    if not isinstance(conversation, dict):
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}] must be an object")
    if "id" not in conversation:
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].id is required")
    if "title" not in conversation:
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].title is required")
    messages = conversation.get("messages")
    if not isinstance(messages, list):
        raise ValueError(f"Invalid supported-format structure: conversations[{conv_idx}].messages must be a list")
    for msg_idx, message in enumerate(messages):
        _validate_message(message, conv_idx, msg_idx)


def parse_export_json(raw_text: str) -> dict[str, Any]:
    """Parse and validate the Phase 1 supported export schema."""
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc.msg}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("Invalid supported-format structure: top-level JSON must be an object")

    conversations = parsed.get("conversations")
    if not isinstance(conversations, list):
        raise ValueError("Invalid supported-format structure: top-level 'conversations' must be a list")

    for conv_idx, conversation in enumerate(conversations):
        _validate_conversation(conversation, conv_idx)

    return parsed

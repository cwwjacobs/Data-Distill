# Supported Format (Phase 1)

Phase 1 supports exactly one JSON schema: a top-level object containing a `conversations` list.

## Required top-level shape
```json
{
  "conversations": [ ... ]
}
```

## Required conversation fields
Each conversation entry in `conversations` must be an object with:
- `id`
- `title`
- `messages` (list)

## Required message fields
Each message in `messages` must be an object with:
- `role`
- `content`

`timestamp` is accepted when present. Additional fields are allowed and preserved in raw payloads.

## Phase 1 constraints
- Only this schema is supported.
- Any unsupported top-level structure raises `ValueError`.
- No multi-format detection is performed.

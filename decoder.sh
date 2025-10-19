#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <operation pipeline> <fragment>" >&2
  exit 1
fi

pipeline=$1
fragment=$2

python - "$pipeline" "$fragment" <<'PY'
import base64
import binascii
import codecs
import re
import sys

def rot47(text: str) -> str:
    result = []
    for ch in text:
        code = ord(ch)
        if 33 <= code <= 126:
            result.append(chr(33 + ((code - 33 + 47) % 94)))
        else:
            result.append(ch)
    return "".join(result)


def parse_xor_key(raw: str) -> bytes:
    raw = raw.strip()
    if not raw:
        raise ValueError("Empty XOR key")

    if (raw[0] == raw[-1]) and raw[0] in "'\"":
        raw = raw[1:-1]
        raw = raw.encode("latin1", "surrogatepass").decode("unicode_escape")

    lowered = raw.lower()
    if lowered.startswith("0x"):
        try:
            return bytes([int(lowered, 16) & 0xFF])
        except ValueError as exc:
            raise ValueError(f"Invalid hexadecimal XOR key: {raw}") from exc

    if raw.isdigit():
        value = int(raw)
        if not 0 <= value <= 255:
            raise ValueError("Numeric XOR key must be between 0 and 255")
        return bytes([value])

    return raw.encode("latin1")


def apply_operation(data: bytes, operation: str) -> bytes:
    op = operation.strip()
    upper = op.upper()

    if upper == "HEX":
        try:
            return binascii.unhexlify(data.decode("latin1"))
        except (binascii.Error, ValueError) as exc:
            raise ValueError(f"Invalid HEX data: {data!r}") from exc

    if upper == "BASE64":
        try:
            return base64.b64decode(data, validate=True)
        except binascii.Error as exc:
            raise ValueError(f"Invalid BASE64 data: {data!r}") from exc

    if upper == "REVERSE":
        return data[::-1]

    if upper == "ROT13":
        decoded = data.decode("latin1")
        return codecs.decode(decoded, "rot_13").encode("latin1")

    if upper == "ROT47":
        decoded = data.decode("latin1")
        return rot47(decoded).encode("latin1")

    match = re.match(r"(?i)XOR\s+KEY\s+(.+)", op)
    if match:
        key_bytes = parse_xor_key(match.group(1))
        if not key_bytes:
            raise ValueError("Empty XOR key after parsing")
        key_len = len(key_bytes)
        return bytes(b ^ key_bytes[i % key_len] for i, b in enumerate(data))

    raise ValueError(f"Unknown operation: {operation}")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("decoder requires exactly two arguments")

    pipeline = [part.strip() for part in sys.argv[1].split('|') if part.strip()]
    if not pipeline:
        raise SystemExit("No operations provided")

    data = sys.argv[2].encode("latin1")

    for operation in reversed(pipeline):
        data = apply_operation(data, operation)

    try:
        decoded = data.decode("utf-8")
    except UnicodeDecodeError:
        decoded = data.decode("latin1")

    sys.stdout.write(decoded)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
PY

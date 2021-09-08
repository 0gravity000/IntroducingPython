# 7.2.4 binasciiによるバイト/文字列の変換
import binascii
valid_png_header = b'\x89PNG\r\n\xla\n'
print(binascii.hexlify(valid_png_header))

print(binascii.unhexlify(b'89504e470d0a1a0a'))
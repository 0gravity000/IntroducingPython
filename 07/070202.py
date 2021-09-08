# 7.2.2 structによるバイナリデータの変換
import struct
valid_png_header = b'\x89PNG\r\n\xla\n'
data = b'\x89PNG\r\n\xla\n\x00\x00\x00\rIHDR' * \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8f\x08\x02\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'hegith', height)
else:
    print('Not a valid PNG')
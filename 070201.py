# 7.2.1 バイトとバイト列
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes

the_byte_array = bytearray(blist)
the_byte_array

# エラー bytes変数は書き換えできない
the_bytes[1] = 127

# bytearray変数は書き換えできる
the_byte_array[1] = 127
the_byte_array

the_bytes = bytes(range(0, 256))
the_byte_array= bytearray(range(0, 256))
the_bytes
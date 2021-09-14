# 7-1
import unicodedata
mystery = '\U0001f4a9'
mystery
unicodedata.name(mystery)

# 7-2
pop_bytes = mystery.encode('utf-8')
pop_bytes

# 7-3
pop_string = pop_bytes.decode('utf-8')
pop_string
pop_string == mystery

# 7-4
poem = '''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s.
'''
args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)

# 7-5
letter = '''
Dear {salution} {name}

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it should be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests, is {percent}% 
less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

# 7-6
response = {
  'salution': 'Colonel',
  'name': 'Hackenbush',
  'product': 'duck blind',
  'verbed': 'imploded',
  'room': 'conservatory',
  'animals': 'emus',
  'amount': '$1.38',
  'percent': '1',
  'spokesman': 'Edger Schmeltz',
  'job_title': 'Licensed Podistrist'
}
print(letter.format(**response))

# 7-7
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

# 7-8
# 'c'で始まるすべての単語を抽出
# \bは、単語と非単語の境界を先頭とするという意味。単語の先頭か末尾を指定するために使う
# cは、探している単語の先頭文字
# \wは、任意の単語文字。つまり英数字とアンダースコア(_)である
# *は、前の単語文字が0個以上という意味
# 先頭のクオートの右にあるrが必要。ないと\bをバックスペースと解釈してしまう
import re
pat = r'\bc\w*'
re.findall(pat, mammoth)

# 7-9
# 'c'で始まるすべての4文字の単語を抽出
pat = r'\bc\w{3}\b'
re.findall(pat, mammoth)

# 単語の末尾を示すために最後の\bは必要
# 最後の\bがないと'c'で始まるすべての単語の先頭4文字が返される
pat = r'\bc\w{3}'
re.findall(pat, mammoth)

# 7-10
# rで終わるすべての単語を抽出
pat = r'\b\w*r\b'
re.findall(pat, mammoth)

# しかし、lで終わる単語を得ようとすると、変な結果になる
# you'llの’ll’がヒットする
# これは\wというパターンは、英数字とアンダースコアにしかマッチしないため
# つまりASCIIのアポストロフィにはマッチしないため
pat = r'\b\w*l\b'
re.findall(pat, mammoth)

# これで'you'll'がヒットする
# アポストロフィはバックスラッシュでエスケープする
pat = r'\b[\w\']*l\b'
re.findall(pat, mammoth)
# またはパタン文字列をダブルクォートで囲んでもOK
pat = r"\b[\w']*l\b"
re.findall(pat, mammoth)

# でもこれだとNG
pat = r'\b[\w']*l\b'
re.findall(pat, mammoth)

# 7-11
# 3個の連続した母音を含むすべての単語を返す
pat = r"\b\w*[aeiou]{3}[^aeiou]\w*\b"
re.findall(pat, mammoth)

# 'beau\nIn'がヒットしてしまうので
# 以下のようにすると'beau'がヒットする
pat = r"\b\w*[aeiou]{3}[^aeiou\s]*\w*\b"
re.findall(pat, mammoth)

# 7-12
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + \
  '040000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
len(gif)

# 7-13
gif[:6] == b'GIF89a'

# 7-14
import struct
width, geight = struct.unpack('<HH)', gif[6:10])
width, geight

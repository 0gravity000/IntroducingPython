# 7.1.1.1 Python3のUnicode文字列
def unicode_test(value):
    '''名前は、以下を参照
    https://www.unicode.org/charts/charindex.html
    '''
    import unicodedata  #モジュールのインポート
    # 名前(大文字と小文字を区別しない)を与えるとUnicode文字が返される
    name = unicodedata.name(value)
    # Unicode文字列を与えると大文字の名前が返される
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

# 文字を渡すと名前が返る
unicode_test('A')
unicode_test('$')
# Unicodeを渡すと名前が返る
unicode_test('\u00a2')
unicode_test('\u00ac')
unicode_test('\u2603')

# Webサイトからコピペしたcaféがうまく動くなら
# UTF-8でエンコーディングされたものだから
place = 'café'
place

import unicodedata
unicodedata.name('\u00e9')

# https://www.unicode.org/charts/charindex.html
# unicodedata.lookup('E WITH ACUTE, LATIN CAPITAL LETTER')    #これだとエラー
# カンマを削除して、前後を逆にする
unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE')
unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')

place = 'caf\u00e9'
place
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place
u_umlaut = '\N{LATIN CAPITAL LETTER U WITH DIAERESIS}'
u_umlaut
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'on a', place)

# 文字列のlen()はバイト数でなく、Unicodeの文字数を数える
len('$')
len('\U0001f47b')
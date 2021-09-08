# 7.1.1.1 Python3のUnicode文字列
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s", % (value, name, value2)')

unicode_test('A')

unicode_test('$')

unicode_test('\u00a2')

unicode_test('\u00ac')

unicode_test('\u2603')

#
place = 'café'
place

import unicodedata
unicodedata.name('\u00e9')

# https://www.unicode.org/charts/charindex.html
# unicodedata.lookup('E WITH ACUTE, LATIN CAPITAL LETTER')    #これだとエラー
unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE')    #これだとエラー

place = 'caf\u00e9'
place

place = 'caf\n(LATIN CAPITAL LETTER E WITH ACUTE)'
place

#
u_umlaut = '\n(LATIN CAPITAL LETTER U WITH DIAERESIS)'
u_umlaut

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'on a', place)

len('$')

len('\u0001f47b')
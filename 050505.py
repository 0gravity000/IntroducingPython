# 5.5.5 itertoolsによるコード構造の反復処理
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

#
import itertools
for item in itertools.cycle([1, 2]):
    print

#
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

#
import itertools
def multiply(a, b):
    return a + b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
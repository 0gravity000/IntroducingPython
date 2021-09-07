# 8.1.5 withによるファイルの自動的なクローズ
poem = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a return on the previos night.'''

with open('relativity', 'wt') as fout:
    fout.write(poem)
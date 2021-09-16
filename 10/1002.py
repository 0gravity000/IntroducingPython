# 10.2 ディレクトリ
# 10.2.1 mkdir()による作成
import os
os.mkdir('poems')
os.path.exists('poems')

# 10.2.2 rmdir()による削除
os.rmdir('poems')
os.path.exists('poems')


# 10.2.3 listdir()による内容リストの作成
os.mkdir('poems')
os.listdir('poems')
os.mkdir('poems/mcintyre')
os.listdir('poems')

fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''cheeful and happy was his mood,''')
fout.close()
os.listdir('poems/mcintyre')


# 10.2.4 chdir()によるカレントディレクトリの変更
os.chdir('poems')
os.listdir('.')

# 10.2.5 glob()によるパターンにマッチするファイルのリストの作成
# glob()はUnixシェルの規則を使って、ファイル、ディレクトリ名のパターンマッチを行う
import glob
# mで始まるファイル、ディレクトリのリスト
glob.glob('m*')
# 2文字の名前を持つファイル、ディレクトリ
glob.glob('??')
# mで始まりeで終わる8文字のファイル、ディレクトリ
glob.glob('m??????e')
# k,l,mのどれかで始まりeで終わるファイル、ディレクトリ
glob.glob('[klm]*e')


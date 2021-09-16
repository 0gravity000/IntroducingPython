# 10.1 ファイル
# 10.1.1 open()による作成
fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

# 10.1.2 exists()によるファイルが存在することのチェック
import os
os.path.exists('oops.txt')
os.path.exists('./oops.txt')
os.path.exists('waffles')
os.path.exists('.') #カレントディレクトリ
os.path.exists('..')  #親ディレクトリ

# 10.1.3 isfile()によるファイル・タイプのチェック
name = 'oops.txt'
# ファイルかどうか？
os.path.isfile(name)
# ディレクトリかどうか
os.path.isdir(name)
# 絶対パス名かどうか
os.path.isabs(name)
os.path.isabs('/big/fake/name')
os.path.isabs('/big/fake/name/without/a/leading/slash')

# 10.1.4 copy()によるコピー
import shutil
shutil.copy('oops.txt', 'ohno.txt')

# 10.1.5 rename()によるファイル名の変更
import os
os.rename('ohno.txt', 'ohwell.txt')

# 10.1.6 link()、symlink()によるリンク作成
# 新しいyikes.txtファイルから既存のoops.txtファイルへのハードリンクを作る
os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')
# 新しいjeepers.txtファイルから既存のoops.txtファイルへのシンボリックリンクを作る
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt') # OSError: [WinError 1314] クライアントは要求された特権を保有していません。
# windowsではシンボリックリンクは作成できないっぽい
# https://minerva.mamansoft.net/Notes/Windows%E3%81%A7%E3%82%B7%E3%83%B3%E3%83%9C%E3%83%AA%E3%83%83%E3%82%AF%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E4%BD%9C%E6%88%90%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB%E3%81%99%E3%82%8B%E8%A8%AD%E5%AE%9A

# 10.1.7 chmod()のよるパーミッションの変更
os.chmod('oops.txt', 0o400)
# or
import stat
os.chmod('oops.txt', stat.S_IRUSR)

# 10.1.8 chown()によるオーナーの変更
uid = 5
gid = 22
import os
os.chown('oops', uid, gid)  # AttributeError: module 'os' has no attribute 'chown'
# windowsではエラーになる？

# 10.1.9 abspath()によるパス名の取得
# 相対パスを絶対パスにする
import os
os.path.abspath('oops.txt')

# 10.1.10 realpath()によるシンボリックリンクパス名の取得
os.path.realpath('jeepers.txt')

# 10.1.11 remove()によるファイルの削除
os.remove('oops.txt')
os.path.exists('oops.txt')


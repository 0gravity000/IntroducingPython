# 10.3 プログラムとプロセス
# プログラムを実行すると、OSはプロセスを1つ作る
# プロセスはシステムリソース(CPU、メモリ、ディスクスペース)と
# OSのカーネルのデータ構造(ファイル、ネットワーク接続、利用統計など)を使う

import os
# 実行されているPythonインタープリタのプロセスIDを取得する
os.getpid()
# 実行されているPythonインタープリタのカレントディレクトリを取得する
os.getcwd()
# ユーザーIDを取得する Windowsには、uid／gidに相当する情報が存在しない？
os.getuid()
# グループIDを取得する Windowsには、uid／gidに相当する情報が存在しない？
os.getgid()

# 10.3.1 subprocessによるプロセスの作成
# 標準ライブラリのsubprocessモジュールを使えば、
# Pythonからほかのプログラムを起動、終了することができる

# Unixのdateの結果を出力
import subprocess
ret = subprocess.getoutput('date')
ret

ret = subprocess.getoutput('date -u')
ret

ret = subprocess.getoutput('date -u | wc')
ret

ret = subprocess.check_output(['date', '-u'])
ret

ret = subprocess.getstatusoutput('date')
ret

ret = subprocess.call('date')
ret

ret = subprocess.call('date -u', shell=True)
ret = subprocess.call(['date', '-u'])

# 10.3.2 multiprocessingによるプロセスの作成
# mp.py
# python mp.py
import multiprocessing
import os

def do_this(what):
  whoami(what)

def whoami(what):
  print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
  whoami("I'm the main program")
  for n in range(4):
    p = multiprocessing.Process(target=do_this,
    args=("I'm fucction %s" % n,))
    p.start()

# 10.3.3 terminate()によるプロセスの強制終了
# mp1.py
# python mp1.py
import multiprocessing
import time
import os

def whoami(name):
  print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
  whoami(name)
  start = 1
  stop = 100000
  for num in range(start, stop):
    print("\tNumber %s of %s, Honk!" % (num, stop))
    time.sleep(1)

if __name__ == "__main__":
  whoami("main")
  p = multiprocessing.Process(target=loopy, args=("loopy",))
  p.start()
  time.sleep(5)
  p.terminate()


# 8.2.7 設定ファイル
# settings.cfg
[english]
greeting = Hello

[french]
greeting = Bonjour

[files]
home = /usr/local
# 単純な挿入
bin = %(home)s/bin

#
import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

cfg

cfg['french']

cfg['french']['greeting']

cfg['files']['bin']
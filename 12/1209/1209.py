# 12.9 エラーメッセージのロギング
# loggingはPython標準のロギングライブラリ

import logging
logging.debug("Looks like rain")
logging.info("And hail")
logging.warn("Did I hear thunder?")
logging.error("Was that lightning?")
logging.critical("Stop fencing and get inside!")

# デフォルトの優先順位レベルはWARNING
# デフォルトレベルは、basicConfig()で設定できる
# 最も低いレベルはDEBUGで、これを設定するとすべてのレベルがログに書かれる

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("It's a raining again")
logging.info("With hail the size of hailstones")
logging.warn("Did I hear thunder?")
logging.error("Was that lightning?")
logging.critical("Stop fencing and get inside!")

# 上記はロガーオブジェクトを作らずに、logging関数だけを使って例
# 以下はロガーオブジェクトを使った例

import logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger('bunyan')
logger.debug('Timber')

# ロガー名にドットが含まれている場合、それはロガーの階層構造でレベルを表す
# そのため、quarkという名前のロガーは、
# quark.charmedという名前のロガーよりも上の階層にある
# 特別なルートロガーが頂点にあり、''という名前になっている

# ハンドラを使えてば、メッセージを別の場所に送り込むことができる
# もっともよく使われる場所はログファイルで次のように指定する
# メッセージは画面に表示されなくなり、
# blue_ox.logというファイルに書き込まれる
# filename引数付きでbasicConfig()をyいびダスト、
# FileHandlerが作られ、ロガーが使えるようになる
# loggingモジュールには、画面やファイルだけでなく
# メッセージをメール、Webサーバーなどに送る少なくとも15種類のハンドラが含まれている
import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('buuyan')
logger.debug("Where's my axe?")
logger.warn("I need my axe")

# ロギングされるメッセージの書式を設定することができる
# basicConfig()にformat文字列を与えると、好みの書式に変更できる
import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('buuyan')
logger.error("Where's my other plaid shirt?")



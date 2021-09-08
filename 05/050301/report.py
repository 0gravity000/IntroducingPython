# 5.3.1 モジュールのインポート
def get_description():
    """プロと同じようにランダムな天気を返す"""
    from random import choice
    possibilies = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilies)
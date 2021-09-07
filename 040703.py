# 4.7.3 デフォルト引数値の指定
def menu(wine, entree, dessert='pudding'):
    return('wine': wine, 'entree': entree, 'dessert': dessert)

menu('chardonnay', 'chicken')

menu('dunkelfelder', 'duck', 'doughnut')

# バグがあるコード
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')

buggy('b')  # ['ｂ']にならないといけない

# 正しいコード
def works(arg):
    result = []
    result.append(arg)
    return result

buggy('a')

buggy('b')  # ['ｂ']が表示される
# 4.7.8 関数内関数
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')
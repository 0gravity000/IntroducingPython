# 4.12 独自例外の作成
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException

#例外オブジェクト時代にアクセスして、情報を表示することもできる
try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)

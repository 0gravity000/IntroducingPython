def dump(func):
  "入力引数と出力値を表示する"
  def wrapped(*args, **kwargs):
    print("Function name: %s" % func.__name__)
    print("Input arguments: %s" %  ' '.join(map(str, args)))
    print("Input Keyword arguments: %s" % kwargs.items())
    output = func(*args, **kwargs)
    print("Output:", output)
    return output
  return wrapped

# 4.5.3 for-elseによるbreakのチェック
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheeses)
    break
else:   # breakしていないということはチーズがないということ
    print('This is not much of a cheese shop, is it?')

# for-elseを使わないコード
cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely', cheeses)
    break

if not found_one:
    print('This is not much of a cheese shop, is it?')
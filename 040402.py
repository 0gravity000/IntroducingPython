# 4.4.2 while-continueによる次のイテレーションの開始
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':    #終了
        break
    number = int(value)
    if number % 2 == 0: #偶数
        continue
    print(number, "squared is", number*number)
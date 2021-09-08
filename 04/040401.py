# 4.4.1 while-breakによるループ中止
while True:
    stuff = input("String to capitalize [Type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
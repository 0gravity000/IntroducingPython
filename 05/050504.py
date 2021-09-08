# 5.5.4 スタック + キュー = デック
def palindroms(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft != dq.pop():
            return False
        return True

palindroms('a')

palindroms('racecar')

palindroms('')

palindroms('halibut')

#
def another_palindroms(word):
    return word == word[::-1]

another_palindroms('radar')

another_palindroms('halibut')
# 4.11 エラー処理とtry、except
short_list = [1, 2, 3]
position = 5
short_list[position]

#try,exceptを用いて例外をキャッチ
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got', position)

# [except exceptiontype as name]
# のようにすれば、nameに例外オブジェクトを格納できる
# これで例外の詳細情報がわかる
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something slse broke:', other)

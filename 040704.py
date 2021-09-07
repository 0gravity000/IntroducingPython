# 4.7.4 *による位置引数のタプル化
def print_args(*args):
    print('Positional argument tuple:', args)

print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

#
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one two:', required2)
    print('All the resr:', args)

print_more('cap', 'aloves', 'scarf', 'monocle', 'mustache wax')
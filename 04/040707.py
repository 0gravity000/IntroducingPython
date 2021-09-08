# 4.7.7 一人前のオブジェクトとしての関数
def answer():
    print(42)

def run_something(func):
    func()

run_something(answer)

type(run_something)

#
def add_args(arg1, arg2):
    print(arg1 + arg2)

type(add_args)

#
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

#
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)


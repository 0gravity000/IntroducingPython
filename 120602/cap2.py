def just_do_it(test):
    # "引数testに含まれるすべての単語をタイトルケースとして返す"
    from string import capwords
    return capwords(test)
    #return test.title()
    #return test.capitalize()
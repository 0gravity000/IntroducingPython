def just_do_it(test):
    """
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a varitable flock of ducks')
    'A Varitable Flock Of Ducks'
    >>> just_do_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """
    from string import capwords
    return capwords(test)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
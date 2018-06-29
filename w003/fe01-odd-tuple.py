def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    new_tup = ()
    for element in aTup[::2]:
        new_tup = new_tup + (element,)
    return new_tup

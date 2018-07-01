def test_used_while_coding():
    assert(is_lower('az?') == True)
    assert(is_lower('aB!z') == False)
    assert(is_upper('UPPER') == True)
    assert(is_upper('NOT UPPEr') == False)
    assert(to_upper('abc')=='ABC')
    assert(to_upper('ABC')=='ABC')
    assert(to_upper('a.b ?c')=='A.B ?C')
    assert(to_lower('aaron') == 'aaron')
    assert(to_lower('AaROn! ') == 'aaron! ')
    assert(to_lower('GRRR?') == 'grrr?')

    assert(get_word('joby the slightly magnificent',9)=='slightly')
    assert(get_word('joby the slightly magnificent',18)=='magnificent')

    assert(to_title('joby the slightly magnificent')== 'Joby the Slightly Magnificent')

    assert(is_alpha('abcXYZ'))
    assert(not is_alpha('ABC '))

def test_leeokus():
    strings = ['harry potter, and the chamber of secrets',
               'HARRY POTTER, AND THE CHA?MBER OF SECRETS',
               '@#%@$%.foo ?BAR ,bAZ',
               'fo.o b.ar B.AZ']
    for s in strings:
        assert(to_title(s) == s.title())

def to_title(s):
    common_words = () # ('a', 'an', 'of', 'the')
    s = to_lower(s)
    for i in range(len(s)):
        if is_alpha(s[i]) and (i==0 or not is_alpha(s[i-1])):
            if get_word(s, i) not in common_words:
                s = s[:i] + to_upper(s[i]) + s[i+1:]
    return s

def to_upper(s):
    for i in range(len(s)):
        if not is_upper(s[i]):
            s = s[:i] + chr(ord(s[i])-32) + s[i+1:]
    return s

def to_lower(s):
    for i in range(len(s)):
        if not is_lower(s[i]):
            s = s[:i] + chr(ord(s[i])+32) + s[i+1:]
    return s



def is_alpha(s):
    if len(s) == 0:
        return False
    for c in s:
        if not ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')):
            return False

    return True

def is_lower(s):
    if len(s) == 0:
        return False
    for c in s:
        if c >= 'A' and c <= 'Z':
            return False
    return True

def is_upper(s):
    if len(s) == 0:
        return False
    for c in s:
        if c >= 'a' and c <= 'z':
            return False
    return True

def get_word(phrase, start):
    for end in range(start, len(phrase)):
       if not is_alpha(phrase[end]):
           return phrase[start:end]
    return phrase[start:]

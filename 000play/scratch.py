''' fisk's implementation '''

def p(n, k=None):
    if k is None:
        k = n
    for i in xrange(int((n*2)**.5), k):
        if n-i <= ((i-1)*i)/2 and n-i >= 0:
            if n-i == 0:
                yield (i,)
            else:
                for j in (p(n-i, i)):
                    yield (i,) + j

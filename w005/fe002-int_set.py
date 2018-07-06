'''
Your task is to define the following two methods for the intSet class:

    Define an intersect method that returns a new intSet containing elements that
    appear in both sets. In other words,

    s1.intersect(s2)

    would return a new intSet of integers that appear in both s1 and s2. Think
    carefully - what should happen if s1 and s2 have no elements in common?

    Add the appropriate method(s) so that len(s) returns the number of elements
    in s.
'''


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    ########################
    # my code starts here: #
    ########################

    def intersect(self, other):
        intersection = intSet()
        for i in self.vals:
            if other.member(i):
                intersection.insert(i)
        return intersection

    def __len__(self):
        return len(self.vals)

def test_intersect():
    a = intSet()
    for i in range(10):
        a.insert(i)
    print(a)

    b = intSet()
    for i in range(8, 20):
        b.insert(i)

    print(b)

    print(b.intersect(a))
    print(a.intersect(b))

    c = intSet()
    for i in range(20, 30):
        c.insert(i)

    print(c)
    print(c.intersect(a))

def test_len():
    a = intSet()
    assert(len(a) == 0)

    for i in range(10):
        a.insert(i)
    assert(len(a) == 10)

def main():
    test_intersect()
    test_len()

if __name__ == '__main__':
    main()

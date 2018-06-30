
def main():
    """
    Learning how to break things
    """

def test_inc():
    assert(inc(3) == 4)
    assert(inc(5) == 6)
    assert(inc(1000000) == 1000001)

def inc(x:int) -> int:
    return x+1

if __name__ == "__main__":
    main()

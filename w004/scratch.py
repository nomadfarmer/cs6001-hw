try:
    a = [0, 1, 2, 3]
    b = a[2]
    c = 19/0
except IndexError:
    print("exception")
else:
    print("else")
finally:
    print("finally")

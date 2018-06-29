def scope_test(L):
    for i in range(len(L)):
        L[i] = 'pwnd'

my_list = [3, 1, 4, 1, 5, 9]
scope_test(my_list)
print(my_list)




def checknum(list):
    return True if set([1, 2, 3]).issubset(set(list)) else False


print(checknum([1, 2, 3]))
print(checknum([1, 2, 4, 5]))
print(checknum([1, 2, 3, 1]))
print(checknum([1, 2]))
print(checknum([0, 4, 5, 1, 2, 3]))

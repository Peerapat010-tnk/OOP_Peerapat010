def num(a,b):
    test = []
    for i in range(a,b+1):
        if i % 3 != 0:
            test.append(i)
    return test
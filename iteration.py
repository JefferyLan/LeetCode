def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        #a, b = b, a + b
        temp = b
        b += a
        a = temp

if __name__ == '__main__':
    n = 10**5
    i = 0
    for x in fibon(n):
        i += 1
    print("total number={}".format(i))
    iter_fibon = iter(fibon(n))
    i = 0
    while True:
        try:
           x = next(iter_fibon)
           i += 1
        except StopIteration:
            print("total number={}".format(i))
            break





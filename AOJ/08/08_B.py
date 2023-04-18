while True:
    x = input()
    if x == '0':
        break
    else:
        a = 0
        for i in x:
            i = int(i)
            a += i
    print("{}".format(a))

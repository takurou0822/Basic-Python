while True:
    x,y = map(int, input().split())
    if x>y:
        print('{} {}'.format(y,x))
    elif x==y==0:
        break
    else:
        print('{} {}'.format(x,y))

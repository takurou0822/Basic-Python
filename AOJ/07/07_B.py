while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    else:

        q = []
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                for c in range(b+1, n+1):
                    if a+b+c == x:

                        q.append('{0} {1} {2}.format(a,b,c) ')  
   
        print(len(q))

n = int(input())
cards=[]

for k in 'SHCD':
    for l in range(1,14):
        
        cards.append("{} {}".format(k,l))

for i in range(n):
   cards.remove(input())

for z in cards:
    print(z)

    


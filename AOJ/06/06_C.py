n=int(input())
room = [[[0]*10 for i in range (3)] for j in range(4)]
for info in range(n):
     b,f,r,v=map(int,input().split())
     room[b-1][f-1][r-1] += v

for a in range(3):
    print (*room[0][a])
print('#'*20) 

for c in range(3):
    print (*room[1][c])
print('#'*20)

for d in range(3):
    print (*room[2][d])
print('#'*20)

for e in range(3):
    print (*room[3][e])
    
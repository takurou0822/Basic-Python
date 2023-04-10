W,H,x,y,r = map(int, input().split())
if (2*r<=x+r <= W and 2*r<=y+r <= H):
    print(f"Yes")
else:
    print (f"No")
S = int(input())
h= int (S / 3600)
m= int((S - h*3600)/60)
s= int (S -h*3600 - m*60)
print(f"{h}:{m}:{s}")
import sys

atai1 = [0]*6
atai2 = [0]*6
input_atai1 = list(map(int, input().split()))
input_atai2 = list(map(int, input().split()))


class Saikoro:        
    # 初期情報を入力
    def __init__(self, h, a): 
        
        self.h = h
        self.a = a       
        for i in range(6):
            self.h[i] = self.a[i] 
            
    def KE(self):                          
        self.h[2], self.h[5], self.h[0], self.h[3] = self.h[0], self.h[2], self.h[3], self.h[5] 
    
    def KN(self):       
        self.h[4], self.h[0], self.h[5], self.h[1] = self.h[0], self.h[1], self.h[4], self.h[5]
    
    def KS(self): 
        self.h[1], self.h[5], self.h[0], self.h[4] = self.h[0], self.h[1], self.h[4], self.h[5]           
    
    def KW(self):
        self.h[3], self.h[0], self.h[5], self.h[2] = self.h[0], self.h[2], self.h[3], self.h[5]

       
date1 = Saikoro(atai1, input_atai1)
date2 = Saikoro(atai2, input_atai2)

for e in range(4):
    date2.KE()
    for n in range(4):
        date2.KN()
        for s in range(4):
            date2.KS()              
            for w in range(4):
                date2.KW()
                
                if atai1 == atai2:
                    print("Yes")
                    sys.exit()

print("No")
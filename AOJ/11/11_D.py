class Saikoro:        
    # 初期情報を入力
    def __init__(self, h): 
        self.h = h
  
    def KE(self):                          
        self.h[2], self.h[5], self.h[0], self.h[3] = self.h[0], self.h[2], self.h[3], self.h[5] 
    
    def KN(self):       
        self.h[4], self.h[0], self.h[5], self.h[1] = self.h[0], self.h[1], self.h[4], self.h[5]
    
    def KS(self): 
        self.h[1], self.h[5], self.h[0], self.h[4] = self.h[0], self.h[1], self.h[4], self.h[5]           
    
    def KW(self):
        self.h[3], self.h[0], self.h[5], self.h[2] = self.h[0], self.h[2], self.h[3], self.h[5]


count = 0


def hikaku(saikoro1, saikoro2):
    
    deta2 = Saikoro(saikoro2)
    for e in range(5):
        deta2.KE()
        for n in range(5):
            deta2.KN()
            for s in range(5):
                deta2.KS()              
                for w in range(5):
                    deta2.KW()
                
                    if saikoro1 == saikoro2:
                        global count
                        count += 1
                        
    # 全パターン比較


n = int(input())
input_list = [[0]*6 for i in range(n)]
for m in range(n):
    input_list[m] = list(map(int, input().split()))

for i in range(n):
    for d in range(1, n):
        if (i+d) <= (n-1):
            hikaku(input_list[i], input_list[i+d])
    

if count == 0:
    print('Yes')

else:
    print('No')

atai = [0]*6
input_atai = list(map(int, input().split()))
direction = input()


class Saikoro:        
    # 初期情報を入力
    def __init__(self, h, a):
        # hとかの引数はself.hのように定義しなおす
        self.h = h
        self.a = a
       
        for i in range(6):
            self.h[i] = self.a[i] 
            # 回転をさせるときの値の変化を追う
    
    def kaiten(self, d):
        self.d = d
        for m in self.d:
            if m == 'E':
                self.h[2], self.h[5], self.h[0], self.h[3] = self.h[0], self.h[2], self.h[3], self.h[5] 

            if m == 'N':
                self.h[4], self.h[0], self.h[5], self.h[1] = self.h[0], self.h[1], self.h[4], self.h[5]

            if m == 'S':
                self.h[1], self.h[5], self.h[0], self.h[4] = self.h[0], self.h[1], self.h[4], self.h[5]           
            if m == 'W':
                self.h[3], self.h[0], self.h[5], self.h[2] = self.h[0], self.h[2], self.h[3], self.h[5]

        print(self.h[0])
    # date1 というケースをつくってSikoroの規格で生成　その時初期値は＿＿init__の引数で用いたものを当てはめて書いてあげる
    # __init__で引数として用いてあげたもの（ex h)とかは次のメインの関数であらためて書いてあげる必要はない


date1 = Saikoro(atai, input_atai)
date1.kaiten(direction)

def calculation(a,op,b):
  a=int(a)
  b=int(b)
  if op=='+':
       print (a + b)
  elif op=='-':
       print (a - b)
  elif op=='*':
       print (a * b)
  elif op=='/':
       print (int(a / b))
      
 
i = 1
while i > 0:
    ipt = input().split()
    a = ipt[0]
    op = ipt[1]
    b = ipt[2]
    if op == '?':
     break
    calculation(a,op,b)
    
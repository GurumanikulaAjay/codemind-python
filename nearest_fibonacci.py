a=int(input())
fa=x=y=0
fb=1
fn=0
fib=[]
for i in range(a):
    fib.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
for i in range(a):
    if(fib[i]<=a and fib[i+1]>=a):
        x=fib[i]
        y=fib[i+1]
        break
if(a-x>y-a):
    print(y)
elif(a-x<y-a):
    print(x)
elif(a-x==y-a):
    print(x,y)
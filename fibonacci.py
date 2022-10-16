n=int(input())
fa=0
fb=1
fn=0
a=[]
for i in range(n):
    a.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(*a)
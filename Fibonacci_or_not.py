n=int(input())
fa=0
fb=1
fn=0
a=[]
for i in range(100):
    a.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
if n in a:
    print(True)
else:
    print(False)
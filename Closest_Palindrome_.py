def pal(d):
    q=str(d)
    q=q[::-1]
    q=int(q)
    if d==q:
        return 1
    return 0
n=int(input())
w=0
x=0
for i in range(n-1,10,-1):
    if pal(i)==1:
        w=i
        break
for j in range(n+1,10000):
    if pal(j)==1:
        x=j
        break
if n-w < x-n:
    print(w)
elif(n-w)==(x-n):
    print(w,x)
else:
    print(x)
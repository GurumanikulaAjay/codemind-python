def rev(r,s):
    r=r[s-1::-1]
    return r
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    r=input()
    x=s
    while(x>0):
        r=rev(r,s)+r[s::]
        s-=1
        x-=1
    print(r)
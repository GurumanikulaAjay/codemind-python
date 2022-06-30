n=int(input())
a=list(map(int,input().split()))
if a.count(a[0])==n:
    print(0)
else:
    v=0
    for i in range(n):
        if a.count(a[i])>v:
            v=a.count(a[i])
    print(v)
    
        
    
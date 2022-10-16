
n=int(input())
a=list(map(int,input().split()))
if len(a)<=2:
    print("no")
else:
    c=0
    for i in range(2,n):
        if a[i]==a[i-1]+a[i-2]:
            c+=1
    if c==n-2:
        print("yes")
    else:
        print("no")
        
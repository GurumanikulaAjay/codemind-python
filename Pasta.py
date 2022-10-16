a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
f=1
for i in range(b):
    if brr[i] in arr:
        f=1
        arr.remove(brr[i])
    else:
        f=0
        break
if f==1:
    print("Yes")
else:
    print("No")
def prime(x):
    if x<2:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return o
    return 1
n=int(input())
f=0
for i in range(1,n):
    for j in range(1,n):
        if i*j==n:
            if prime(i)==1 and prime(j)==1:
                f=1
                print(i,j,end=" ")
                break
    if f==1:
        break
if f==0:
    print(-1)
        
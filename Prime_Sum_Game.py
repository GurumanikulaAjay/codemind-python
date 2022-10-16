def prime(x):
    if x<=1:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
            else:
                for i in range(2,int(x**0.5)+1):
                    if x%i==0:
                        return 0
            return 1
a,b,c,d=map(int,input().split())
x=0
for i in range(a,b+1):
    f=0
    for j in range(c,d+1):
        if prime(i+j)==1:
            f=1
    if f==0:
        print("Takahashi")
        break
if f==1:
    print("Aoki")
def prime(x):
    if x<=1:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
    return 1
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i)==0:
        c+=1
print(c)

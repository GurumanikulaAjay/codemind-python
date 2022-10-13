def prime(x):
    if x<2:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i)==1:
        c+=1
print(c)
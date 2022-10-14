def pal(x):
    s=str(x)
    rev=s[::-1]
    rev=int(rev)
    if rev==x:
        return 1
    return 0
def prime(x):
    if x<=1:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
        return 1
n=int(input())
for i in range((n+1),100000):
    if pal(i)==1 and prime(i)==1:
        print(i)
        break
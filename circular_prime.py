def prime(x):
    if x<2:
        return 0
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
    return 1
n=int(input())
if prime(n)==1:
    r=str(n)
    r=r[::-1]
    r=int(r)
    if prime(r)==1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
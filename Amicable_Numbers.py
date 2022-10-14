def fact(m):
    s=0
    for i in range(1,m):
        if m%i==0:
            s+=i
    return s
m=int(input())
n=int(input())
if fact(m)==n and fact(n)==m:
    print("Amicable")
else:
    print("Not Amicable")
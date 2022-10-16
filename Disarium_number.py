n=int(input())
q=str(n)
l=len(q)
q=int(q)
s=0
while n:
    r=n%10
    s+=r**l
    l-=1
    n=n//10
if s==q:
    print(True)
else:
    print(False)
n=int(input())
r=0
temp=n
while n:
    rem=n%10
    r=r*10+rem
    n=n//10
n=temp
if n==r:
    print(True)
else:
    print(False)
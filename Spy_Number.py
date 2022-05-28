n=int(input())
pro=1
sum=0
while n:
    d=n%10
    pro*=d
    sum+=d
    n=n//10
if sum==pro:
    print('Spy Number')
else:
    print('Not Spy Number')
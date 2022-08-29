n=int(input())#1124
temp=n
sum=0
pro=1
r=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
while(temp!=0):
    r=temp%10
    pro=pro*r
    temp=temp//10
if(sum==pro):
    print('Spy Number')
else:
    print('Not Spy Number')
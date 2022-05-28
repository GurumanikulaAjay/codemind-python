n=int(input())
temp=n
sum=0
while(n!=0):
    d=n%10
    n=n//10
    p=1
    for i in range(1,d+1):
        p=p*i
    sum=sum+p
if sum==temp:
    print('The number',sum,'is a strong number')
else:
     print('The number',temp,'is not a strong number')
    
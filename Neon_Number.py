n=int(input())
num=n*n
sum=0
while(num!=0):
    r=num%10
    sum=sum+r
    num=num//10
if(sum==n):
    print('Neon Number')
else:
    print('Not Neon Number')
    
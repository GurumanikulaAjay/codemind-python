n=int(input())
a=0
b=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        break
else:
    a+=1
rev=0
while n:
    d=n%10
    n=n//10
    rev=(rev*10)+d
for i in range(2,int(rev**0.5)+1):
    if rev%i==0:
       break
else:
    b+=1
if(a==0):
    print('not prime')
elif(a!=0 and b==0):
    print('prime but not a circular prime')
elif(a!=0 and b!=0):
    print('circular prime')
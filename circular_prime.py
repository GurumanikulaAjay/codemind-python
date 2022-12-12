def prime(n):
    for i in range(2,int(n**(0.5)+1)):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
temp=n
s=0
while temp>0:
    r=temp%10
    s=s*10+r
    temp=temp//10
if(prime(n) and prime(s)):
    print('circular prime')
elif(prime(n)==True and prime(s)==False):
    print('prime but not a circular prime')
else:
    print("not prime")
    
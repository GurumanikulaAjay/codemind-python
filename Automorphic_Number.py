import math
n=int(input())
g=n
r=n*n
c=0
while n>0 :
    v=n%10
    c=c+1
    n=n//10
x=r% math.pow(10,c)
if(x==g) :
    print('Automorphic Number')
else :
    print('Not an Automorphic Number')
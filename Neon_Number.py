n=int(input())
sq=n*n
sum=0
while sq:
    d=sq%10
    sum+=d
    sq=sq//10
if sum==n:
    print('Neon Number')
else:
     print('Not Neon Number')
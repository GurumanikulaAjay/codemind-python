n=int(input())
m=int(input())
l=[]
for i in range(n+1,m):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            break
    else:
        l.append(i)
for i in l:
    print(i)
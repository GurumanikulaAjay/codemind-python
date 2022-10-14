a,b=map(int,input().split())
g=l=0
g=max(a,b)
while(True):
    if(g%a==0 and g%b==0):
        l=g
        break
    g+=1
print(l)
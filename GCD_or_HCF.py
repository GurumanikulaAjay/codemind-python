def hcf(x,y):
    if x%y==0:
        return y
    return hcf(y,x%y)
a,b=map(int,input().split())
print(hcf(a,b))
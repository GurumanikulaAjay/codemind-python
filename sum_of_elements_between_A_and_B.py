


n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in a:
    if i>=c and i<=d:
        s+=i
print(s)
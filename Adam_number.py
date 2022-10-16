n=int(input())
v=n**2
v=str(v)
n=str(n)
n=n[::-1]
n=int(n)
x=n**2
x=str(x)
if x==v[::-1]:
    print(True)
else:
    print(False)
n=int(input())
v=str(n)
r=n**2
r=str(r)
if r.endswith(v):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
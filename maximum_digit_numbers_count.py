a=int(input())
b=input()
arr=list(b.split())
x=""
mi=-100
for i in arr:
    if len(i)>mi:
         mi=len(i)
c=0
for i in arr:
    if len(i)==mi:
        print(i,end=" ")
   

s=input()
s=s.lower()
temp=set(s)
l=[]
for i in temp:
    if i==" ":
        continue
    elif(s.count(i)==1):
        l.append(i)
for i in sorted(l):
    print(i,end="")
    
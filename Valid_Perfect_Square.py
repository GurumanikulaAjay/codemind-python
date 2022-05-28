a=int(input())
for i in range(a):
    b=int(input())
    for j in range(b+1):
      if j*j==b:
         print(True)
         break
    else:
        print(False)
         
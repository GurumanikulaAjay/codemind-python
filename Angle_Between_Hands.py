n=input()
hour=m=0
hour=(ord(n[0])-48)*10+(ord(n[1])-48)
m=(ord(n[3])-48)*10+(ord(n[4])-48)
angle=0
if m%2==0:
    angle=30*hour-((11*m)//2)
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))
else:
    angle=30*hour-(5.5*m)
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))
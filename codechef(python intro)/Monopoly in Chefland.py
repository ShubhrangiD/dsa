# Monopoly in Chefland
for i in range (int(input())):
    x,y,z=map(int,input().split())
    if(x>(y+z)):
        print("Yes")
    elif(y>(x+z)):
        print("Yes")
    elif(z>(y+x)):
        print("Yes")
    else:
        print("No")

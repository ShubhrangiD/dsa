# valid triangle
for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=x+y+z
    if(a==180):
        print("YES")
    else:
        print("NO")

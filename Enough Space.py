# Enough Space
for i in range(int(input())):
    n,x,y=map(int,input().split())
    a=x+(y*2)
    if(n>=a):
        print("YES")
    else:
        print("NO")

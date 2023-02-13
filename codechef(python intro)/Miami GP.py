#Miami GP
for i in range (int(input())):
    x,y=map(int,input().split())
    z=107*x/100
    if(y<=z):
        print("YES")
    else:
        print("NO")

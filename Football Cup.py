# Football Cup
for i in range(int(input())):
    x,y=map(int,input().split())
    if(x==0) and (y==0):
        print("NO")
    elif(x!=y):
        print("NO")
    else:
        print("YES")

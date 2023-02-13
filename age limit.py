#age limit
for i in range(int(input())):
    x,y,a=map(int,input().split())
    if(x<=a<y):
        print("YES")
    else:
        print("NO")

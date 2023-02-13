#Max minus Min
for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=min(a,b,c)
    y=max(a,b,c)
    print(y-x)

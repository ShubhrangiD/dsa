# Programming Languages
for i in range(int(input())):
    a,b,a1,b1,a2,b2=map(int,input().split())
    s=min(a,b)
    t=min(a1,b1)
    u=min(a2,b2)
    v=max(a,b)
    w=max(a1,b1)
    x=max(a2,b2)
    if(s==t) and (v==w):
        print(1)
    elif(s==u) and (v==x):
        print(2)
    else:
        print(0)

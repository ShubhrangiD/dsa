#motivation
for i in range(int(input())):
    n,x=map(int,input().split())
    l=[]
    for j in range(n):
        a,b=map(int,input().split())
        if(a<=x):
            l.append(b)
    print(max(l))

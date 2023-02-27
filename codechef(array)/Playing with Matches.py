#Playing with Matches
for i in range(int(input())):
    a,b=map(int,input().split())
    s=a+b
    c=0
    e=0
    l=[]
    v={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    while (s):
        c=s%10
        s//=10
        l.append(c)
    for j in range(len(l)):
        if l[j] in v:
            e=v.get(l[j])+e
    print(e)

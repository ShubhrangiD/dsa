# Chef and Spells
for i in range(int(input())):
    a,b,c=map(int,input().split())
    d=a+b
    e=b+c
    f=a+c
    print(max(d,e,f))

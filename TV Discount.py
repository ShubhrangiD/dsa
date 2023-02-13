#TV Discount
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    e=a-c
    f=b-d
    if(e==f):
        print("Any")
    elif(min(e,f)==e):
        print("First")
    elif(min(e,f)==f):
        print("Second")

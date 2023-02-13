#Bucket and Water Flow
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    e=b-a
    f=c*d
    if(e>f):
        print("Unfilled")
    elif(e==f):
        print("filled")
    else:
        print("overflow")

# Smallest Possible Whole Number
for i in range(int(input())):
    x,y=map(int,input().split())
    a=x-y
    b=a-y
    if(x<y):
        print(x)
    elif(x==y):
        print(0)
    else:
        print(b)

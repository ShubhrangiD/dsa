# Tasty Decisions
for i in range(int(input())):
    x,y=map(int,input().split())
    a=(2*x)
    b=(5*y)
    if(a>b):
        print("Chocolate")
    elif(a==b):
        print("Either")
    else:
        print("Candy")

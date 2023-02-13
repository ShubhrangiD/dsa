#Bull or Bear
for i in range(int(input())):
    x,y=map(int,input().split())
    if(x>y):
        print("LOSS")
    elif(x==y):
        print("NEUTRAL")
    else:
        print("PROFIT")

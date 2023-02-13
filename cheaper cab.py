#cheaper cab
for _ in range (int(input())):
    X,Y=map(int,input().split())
    if(X<Y):
        print("FIRST")
    elif(X==Y):
        print("ANY")
    else:
        print("SECOND")

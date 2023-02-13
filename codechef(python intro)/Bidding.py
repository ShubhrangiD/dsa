# Bidding
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a<c) and (b<c):
        print("Charlie")
    elif(b<a) and (c<a):
        print("Alice")
    elif(c<b) and (a<b):
        print("Bob")

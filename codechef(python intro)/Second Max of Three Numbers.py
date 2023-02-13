#Second Max of Three Numbers
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a<b<c):
        print(b)
    elif(b<c<a):
        print(c)
    elif(a<c<b):
        print(c)
    elif(c<a<b):
        print(a)
    elif(b<a<c):
        print(a)
    elif(c<b<a):
        print(b)

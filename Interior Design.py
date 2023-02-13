# Interior Design
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if((a+b)<=(d+c)):
        print(a+b)
    else:
        print(c+d)

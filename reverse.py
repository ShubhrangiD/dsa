for i in range(int(input())):
    x=int(input())
    r=0
    while(x):
        n=x%10
        r=10*r+n
        x=int(x/10)
    print(r)

for i in range(int(input())):
    x=int(input())
    four=0
    while(x):
        a=int(x%10)
        if (a==4):
            four+=1
        x=int(x/10)
    print(four)

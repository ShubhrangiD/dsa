# Counting Pretty Numbers
for i in range(int(input())):
    n=0
    l,r=map(int,input().split())

    for j in range(l,r+1):
        if (j%10==2) or (j%10==3):
            n+=1
        elif(j%10==9):
            n+=1
    print(n)

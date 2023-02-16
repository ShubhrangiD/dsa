# Rearranging digits to get a multiple 5
for i in range(int(input())):
    l=[]
    f=0
    n=int(input())
    s=int(input())
    while(s):
        a=s%10
        s=s//10
        l.append(a)
    for j in range(0,n):
        if (l[j]%5==0) or (l[j]==0):
            f=1
    if (f==1):
        print("Yes")
    else:
        print("No")

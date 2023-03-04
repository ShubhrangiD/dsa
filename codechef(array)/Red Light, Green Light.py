# Red Light, Green Light
for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for j in range(0,n):
        if (a[j]>k):
            c+=1
    print(c)

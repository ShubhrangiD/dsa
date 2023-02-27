#Problems in your to-do list
for i in range(int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    s=0
    for j in range(0,x):
        if(a[j]>=1000):
            s+=1
    print(s)

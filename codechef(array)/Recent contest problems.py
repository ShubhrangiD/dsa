# Recent contest problems
for i in range(int(input())):
    n=int(input())
    s=0
    l=0
    a=list(map(str,input().split()))
    for j in range(0,n):
        if(a[j]=='START38'):
            s+=1
        else:
            l+=1
    print(s,l)

# The Two Dishes
for i in range(int(input())):
    n,s=map(int,input().split())
    if(s<=n):
        print(s)
    else:
        print((n-s)+n)

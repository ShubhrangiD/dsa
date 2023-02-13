#Monthly Budget
for i in range(int(input())):
    a,b=map(int,input().split())
    if((30*b)<=a):
        print("YES")
    else:
        print("NO")

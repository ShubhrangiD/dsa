#Rating Improvement
for i in range(int(input())):
    x,y=map(int,input().split())
    if(x<=y<=(x+200)):
        print("YES")
    else:
        print("NO")

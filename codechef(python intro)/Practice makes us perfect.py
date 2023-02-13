# Practice makes us perfect
p=list(map(int,input().split()))
n=0
for i in range(0,4):
    if(int(p[i])>=10):
        n+=1
print(n)

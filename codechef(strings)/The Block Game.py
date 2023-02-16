# The Block Game
for i in range(int(input())):
    m=0
    n=input()
    k=''
    for j in n:
        k=j+k
    if(n==k):
        print("wins")
    else:
        print("loses")

# Chef and Dolls
for i in range(int(input())):
    l=[]
    for i in range(int(input())):
        a=int(input())
        l.append(a)
    for j in l:
        if l.count(j)%2!=0:
            print(j)
            break

#Mario and the Broken String
for i in range(int(input())):
    n=int(input())
    s=str(input())
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    if(n%2==0):
        if (s1==s2):
            print("YES")
        else:
            print("NO")

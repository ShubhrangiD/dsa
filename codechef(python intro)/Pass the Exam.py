# Pass the Exam
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if((x+y+z)>=100) and (min(x,y,z)>=10):
        print("PASS")
    else:
        print("FAIL")

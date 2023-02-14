#Easy Pronunciation
import re
regex=r'[bcdfghjklmnpqrstvwxyz]{4,}'
for i in range(int(input())):
    n=int(input())
    s=input()
    match=re.search(regex,s)
    if(match==None):
        print("Yes")
    else:
        print("No")

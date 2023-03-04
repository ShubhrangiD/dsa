# The Lead Game
n=int(input())
wx=0
wy=0
lead=0
for i in range(n):
    x,y=map(int,input().split())
    wx=x+wx
    wy=y+wy
    d=wx-wy
    if(d>0)and(d>lead):
        leader=1
        lead=d
    elif(d<0)and(abs(d)>lead):
        leader=2
        lead=abs(d)
print(leader,lead)

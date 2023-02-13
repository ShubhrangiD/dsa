# Vaccine Dates

for i in range(int(input())):
    x,y,z=map(int,input().split())
    if(y<=x<=z):
        print("Take second dose now")
    elif(y>x):
        print("Too Early")
    else:
        print("Too Late")

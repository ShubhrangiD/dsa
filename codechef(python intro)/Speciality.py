#Speciality
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if(max(x,y,z)==x):
        print("Setter")
    if(max(x,y,z)==y):
        print("Tester")
    if(max(x,y,z)==z):
        print("Editorialist")

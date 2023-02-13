# Id and Ship
for i in range(int(input())):
    x=input()
    if(x=="B")or (x=="b"):
        print("BattleShip")
    elif(x=="C")or(x=="c"):
        print("Cruiser")
    elif(x=="D")or(x=="d"):
        print("Destroyer")
    else:
        print("Frigate")

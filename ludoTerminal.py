#Ludo Game

n = int(input("enter number of players:"))
players=[]
for i in range(0,n):
    print("enter player",i)
    name = input(":")
    players.append(name)
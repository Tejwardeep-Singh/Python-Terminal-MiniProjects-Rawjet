# Multiplayer Dice Game

import random

players=[]
count=[]
flag=False
print("Let's start the game")
n=int(input("enter the number of players:"))
for i in range(0,n):
    print('enter the name of the player',i+1,':',end='')
    name=input('')
    players.append(name)
    count.append(0)

while flag==False:
    for i in range(0,n):
        if 5 in count:
            index = count.index(5)
            winner = players[index]
            print('winner is ', winner)
            flag=True
            break
        else:
            value = random.randint(1,6)
            print("player", players[i]," turn")
            givenValue = int(input("enter the value:"))
            if(givenValue==value):
                print('correct guess')
                count[i]+=1
            else:
                print("wrong guess")

            print("current scores:")
            for i in range(0,n):
                print(players[i],':',count[i])




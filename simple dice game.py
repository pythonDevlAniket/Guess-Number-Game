import random
def dice():
    luck=random.randint(1,6)
    if luck==6:
        print("\n\t$$$ You are lucky...! You got 6 number in dice.. ")
    else:
        print(f"\n\t --->You got {luck} number in dice")
print("\n\t********Welcome to dice game.....Check your luck*******")
dice()
while True:
    hit=int(input("\n\tDid you like this...? Press 1 to play again and 0 to exit the game...>> "))
    if hit==1:
        dice()
    else:
        exit()
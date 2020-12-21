import random  #importing random module
def dice():
    luck=random.randint(1,6)  #generate a random integer between 1 to 6
    if luck==6:
        print("\n\t$$$ You are lucky...! You got 6 number in dice.. ")
    else:
        print(f"\n\t --->You got {luck} number in dice")
print("\n\t********Welcome to dice game.....Check your luck*******")
dice()
while True:
# while loop stop execution if user hits '0'
    hit=int(input("\n\tDid you like this...? Press 1 to play again and 0 to exit the game...>> "))
    if hit==1:
        dice()
    else:
        exit()

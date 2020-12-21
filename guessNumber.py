#The following program will generate a random number and user must predict that number in given number of chances.
#If user fails to get that number then he will lose the game.
import random
print("\n\t\t........Welcome to my Guess number Program........")
n=random.randint(1,11) #this will generate a random integer in range 1 to 11
chances=1
print("\n\tGuess a number between 1 to 11: ",end="")
print("\n\t\tYour Hint is: ",end="")

#The following code is for hint to predict that number
if n%2==0:
    print('''"It is an Even number"''',"\n")
else:
    print('''"It is an Odd number"''',"\n")
print("Lets try it...:",end="")

# If you fails to predict code more than or equal to 5 times then you Lose.. 
while chances<=5:
    guess=int(input()) # takes integer as input
    if guess==n:
        print("\n\t.......Finally you got number",n," in",chances,"chances...!")
        chances=chances+1
        break
    elif guess<n:
        print("\nYour guess was to small:Guess a number higher than",guess)
        print("\n\tGuess again:",end="")
        chances=chances+1
        continue
    else:
        print("\nYour guess was to large:Guess a number smaller than",guess)
        if chances==5:
            break
        else:
            print("\n\tGuess again: ",end="")
            chances=chances+1
            continue

if chances>=5:
    print("\n\tYou Lose...!The number is",n)

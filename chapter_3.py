# Guessing game for chapter 3 - user enters number and script checks if user correctly generated a random number as well as a compile

    #Imports and variables
import random

number = random.randint(1,20)
lives = 6

#
    # HCI stuff

player = input("Hi! Welcome to the MathleDome!!1! What should we announce you as to the screaming fans?\n ?: ")
print("Aaaaand in this corner.... " + player + "!\n")
print(player + ", Choose your weapon! ...In the form of a number between 1 & 20. \n")

# 
    # For loop, or for love

for lives_count in range(1, lives):
    print("Lives", lives_count, "of", lives)
    choice = input("Your Choice?: \n ?: ")
    choice = int(choice)

    if choice < number:
        print("FAILURE. You have dissapointed the fans, and they demand BL00000000D")

    elif choice > number:
        print("No. Overachievers and over guessers will suffer the same fate:\nCHRONIC ANXIETY")
    

    else:
        # print("You live.... today!")
        break

    print()


# 
    # Check for winners, shame the losers

if choice == number:
    lives_count = str(lives_count)
    print("You live, " + player + " -- today! Spend your remaining " +
          lives_count + " lives wisely...")

else:
    number = str(number)
    print("Failure is it's own reward.... For the bloodlust of the FANS!" +
          "\n As you sink slowly into darkness, know that all you had to do was choose " + 
           number + " and you would have stood a chance.")


################################################################################


# Glossary
"""
    number = the number the player must guess
    lives = max_guesses
    lives_count = guess_count
    choice = guess


"""








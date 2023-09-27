# Dice roll Simulator

import random

def no_dice(x):
    sum = 0
    for i in range(x):
        value = random.randint(1,7)
        print(f"Dice {i+1}: {value}")
        sum = sum + value
        
    print(f"Total: {sum}")


x = eval(input("Select number of dices:"))
y= no_dice(x)



# Guess the number game

def game_variables(chances):
    count = 0
    for i in range (chances):
        
        guess = eval(input(f"{i+1} Guess: "))
        if (guess> Upper or guess< Lower):
            print("Enter number within range")
        
        else:
            if guess> number:
                print("Lower")
            else:
                if guess< number:
                    print("Greater")
                else:
                    if guess == number:
                        print("Correct Guess! Guesser Won....")
                        break
        count+=1
        if count == chances:
            print("Chooser Won....")
        else:
            pass

chances=eval(input("How many chances for guesser : "))
Lower = eval(input("Enter the lower limit: "))
Upper = eval(input("Enter the upper limit: "))
number = eval(input("Chooser : Select any number: "))
function_variables = game_variables(chances)

# modifications
# if guess is not in range the chance is not destroyed

                    



# Random password generator

import random
import string

def generate_password(length=12):
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = "123456789"
    special_characters = "@#$"

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = ''.join(random.choices(all_characters, k=length))

    return password

password = generate_password()
print("Generated Password:", password)




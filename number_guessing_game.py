import random 
import time

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have chances to guess the correct number.")

time.sleep(1)

while True:
    difficulty = input("""
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """)

    chances = 0

    if difficulty.lower() in ("easy","1","1.","10","10 chances"):
        chances = 10
        break
    if difficulty.lower() in ("medium","2","2.","5","5 chances"):
        chances = 5
        break
    if difficulty.lower() in ("hard","3.","3","3 chances"):
        chances = 3
        break
    else: continue

difficulty_articulated = {10:"Easy", 5:"Medium", 3:"Hard"}

print("""Great! You have selected the """  + difficulty_articulated[chances] +  """ difficulty level.
Let's start the game! """)

target = (random.randint(1,100))
attempt_count = 0


for number in range(int(chances)):
    guess = int(input("Enter your guess: "))
    attempt_count += 1

    if target > guess:
        print("Incorrect! The number is greater than " + str(guess) + ".")
        continue

    elif target < guess:
        print("Incorrect! The number is less than " + str(guess) + ".")
        continue

    else:
        print("Congratulations! You guessed the correct number in " + str(attempt_count) + " attempts.")
        break

    

    

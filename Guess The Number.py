import random
Number = int(random.randint(1, 20))
guess = None
while guess != Number:
    guess = int(input("Guess the Number from 1 to 20"))
    if guess == Number:
        print("Congrats! You've guessed the number")
        break
    elif guess > Number:
        print("The Number is too High, Try again")
    else:
        print("The Number is too Low, Try again")

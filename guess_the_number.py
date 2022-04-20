import random
import time

def guess(x):
    random_number = random.randint(1, x)
    print("I have my number!", end=" ")
    for tries in range( 3, 0, -1):
        while True:
            try:
                guess = int(input(f"You have {tries} guesses left. Make your guess: "))
            except ValueError:
                print("You're supposed to enter a number!")
                continue
            if guess < 1 or guess > x :
                print(f"Your guess should be a number between 1 and {x}!")
                continue
            else:
                break

        if guess == random_number :
            print("Wow! You guessed right! Well done! :)")
            return
        else:
            print("Mmm... Not the number I was thinking of... Maybe you should try again?")
        
        if tries == 1:
            print("Oh, but you have no tries left. Sorry! :(")
            return 

print("This is 'Guess a Number'")

while True:
    try:
        limit = int(input("Pick an upper limit number: "))
    except ValueError:
        print("You're supposed to enter a number!")
        continue
    if limit < 1 or limit > 65535 :
        print(f"Your guess should be a number between 1 and 65535!")
        continue
    else:
        break

# limit = 5

print(f"I'll pick a number between 1 and {limit}, you'll guess. Are you ready?")
time.sleep(1)

guess(limit)
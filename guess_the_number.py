import random
import time

def guess(x):
    random_number = random.randint(1, x)
    # print("I'm thinking")
    # for i in range (3):
    #     print(".", end ="")
    #     time.sleep(0.5)
    # print(".")
    for tries in range(3,1) :
        print("I'm ready!")
        
        while True:
            try:
                guess = int(input(f"Make your guess! You have {tries} guesses left: "))
            except ValueError:
                print("You're supposed to enter a number!")
                continue
            if guess < 1 or guess > x :
                print(f"Your guess should be a number between 1 and {x}!")
                continue
            else:
                break
        if tries == 1:
            print("You have no tries left. Sorry! :(")
            return 
        elif guess == random_number :
            print("Wow! You guessed right! Well done! :)")
        else:
            print("Mmm... Maybe you should try again.")

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

print(f"You'll guess a number between 1 and {limit}. Ready?")
time.sleep(1)

guess(limit)
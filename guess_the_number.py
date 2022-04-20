import random
import time

def guess(x):
    random_numer = random.randint(1, x)
    guess = int(input("I'm thinking"))
    for i in range (4):
        print(".", end ="")
    for i in range(2):
        print(f"Make your guess! You have {i+1} guesses left.")
        while True:
            try:
                answer=int(input())
            except ValueError:
                print(f"You entered an invalid value! Your guess should be a number between 1 and {x}")
                continue
            else:
                break     


print("This is 'Guess a Number'")
limit = input("Write your limit number: ")

print(f"You'll guess a number between 1 and {limit}. Ready?")
time.sleep(2)
input("Press [enter] to continue")

guess(limit)

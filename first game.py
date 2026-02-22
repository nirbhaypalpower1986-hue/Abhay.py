import random

low = 1
high = 1000

secret = random.randint(low, high)

print("Think of a number between", low, "and", high)

while True:
    guess = int(input("Guess the number: "))

    if guess < low or guess > high:
        print("Out of range! Stay between", low, "and", high)
    elif guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break

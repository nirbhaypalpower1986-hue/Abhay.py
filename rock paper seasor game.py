import random

print("   ROCK PAPER SCISSORS GAME  ")
print('''
r for rock
p for paper
s for scissors
''')

choices = ["r", "p", "s"]

user_win = 0
computer_win = 0
draw = 0

play = "y"

while play == "y":

    computer = random.choice(choices)
    user = input("Enter your choice : ").lower()

    if user not in choices:
        print("INVALID INPUT, choose r / p / s")

    else:
        print("Computer chose:", computer)
        print("You chose:", user)

        if computer == user:
            print("DRAW 😐")
            draw += 1

        elif (user == "r" and computer == "s") or \
             (user == "p" and computer == "r") or \
             (user == "s" and computer == "p"):
            print("YOU WIN 🎉")
            user_win += 1

        else:
            print("COMPUTER WINS 💻")
            computer_win += 1

    play = input("Play again? (y/n): ").lower()

print("\nGAME OVER 👋")
print("Final Score:")
print("You won:", user_win)
print("Computer won:", computer_win)
print("Draws:", draw)
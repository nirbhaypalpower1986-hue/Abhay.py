import random
print("SNAKE WATER GUN \n    GAME")


print("TYPE:\n s for snake\n w for water\n g for gun")


a = ["w","s","g"]
you = input("type : ").lower()
computer = (random.choice(a)).lower()

if you not in a:
	print("SOMETHING WENT WRONG ")
	exit()


j = { "w" : 1,"s" : 0,"g" : -1 }
s = { "w":"water","s":"snake","g":"gun"}
print(f"you chose {s[you] } \n computer choses {s[computer]}")


y = j[you]
c = j[computer]
if you == computer:
	print("it's a draw")
else:
	if (y-c == 2 or y-c == 1):
		print("YOU WINS🎉\n COMPUTER LOSES😔")
	else:
		print("COMPUTER WINS🎉\nYOU LOSES😔")

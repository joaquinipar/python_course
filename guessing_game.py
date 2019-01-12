from random import randint

number = randint(1,10)
win=0
keep="y"
while win!=1 and keep=="y":

	print("Guess a number between 1 and 10!\n")
	answer = int(input())

	if answer == number:
		print("You guessed it! You won!")
		win = 1
	elif answer < number:
		print("Too low mate!")
		print ("Do you want to keep playing? (y/n) ")
		keep = input()
	elif answer > number:
		print("Too high mate!")
		print ("Do you want to keep playing? (y/n) ")
		keep = input()

	if keep == "n":
		break
	



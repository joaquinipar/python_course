from random import randint
print("welcome to paper rock and scissors\n")
print("please enter your choice: ")
answer = input ()


if answer == "rock" or answer == "paper" or answer == "scissors":

	answer_cpu = randint(0,2)
	print(answer_cpu)
	if answer_cpu == 0:
		answer_cpu = "rock"
		print(f"CPU says: {answer_cpu}")
	elif answer_cpu == 1:
		answer_cpu = "paper"
		print(f"CPU says: {answer_cpu}")
	elif answer_cpu == 2:
		answer_cpu = "scissors"
		print(f"CPU says: {answer_cpu}")

	if answer_cpu == answer:
		print("It's a tie!")


	if answer == "rock":
		if answer_cpu == "paper":
			print("You loose!")
		elif answer_cpu == "scissors":
			print("You win!")

	
	if answer == "paper":
		if answer_cpu == "rock":
			print("You win!")
		if answer_cpu == "scissors":
			print("You loose!")

		

	if answer == "scissors":
		if answer_cpu == "rock":
			print("You loose!")
		if answer_cpu == "paper":
			print ("You win!")


	

else:
	print("Try again")
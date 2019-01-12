from random import randint
print("welcome to paper rock and scissors\n")


cpu_win=0
player_win=0
stop =0
while stop!=1:
	print("please enter your choice: ")
	answer = input ()
	
	if answer == "rock" or answer == "paper" or answer == "scissors":
		
		answer_cpu = randint(0,2)
		
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
				cpu_win+=1
			elif answer_cpu == "scissors":
				print("You win!")
				player_win+=1

	
		if answer == "paper":
			if answer_cpu == "rock":
				print("You win!")
				player_win+=1
			if answer_cpu == "scissors":
				print("You loose!")
				cpu_win+=1

		

		if answer == "scissors":
			if answer_cpu == "rock":
				print("You loose!")
				cpu_win+=1
			if answer_cpu == "paper":
				print ("You win!")
				player_win+=1

		
				
	

	else:
		print("Try again")

	print(f"Current status: Player: {player_win} - CPU: {cpu_win}")

	if cpu_win == 2:
		print("CPU WINS!")
		stop =1

	elif player_win ==2:
		print("PLAYER WINS!")
		stop =1

	

# def name_of_function ():
	#stuff that runs

from random import randint

def flip_coin():
	result = randint(0,1)
	if result == 1:
		return "tails"
	else :
		return "head"

def square(num):
	return num**2

def sum_of_odd(list):
	sum=0
	for number in list:

		if number % 2 != 0:
			sum+=number
	print(sum)
	return sum

def sum_of_even(list):
	sum=0
	for number in list:

		if number % 2 == 0:
			sum+=number
	print(sum)
	return sum



#------------------------
print("Let's flip a coin")
print(flip_coin())
#------------------------
print ("let's square a number")
number = int(input() )
square(number)
print(f"The square of {number} is {square(number)}" )

#-----------------------

print("enter numbers to a list")
r_list = []
a=1
while a != "n":
	r_value=int(input())

	r_list.append(r_value)

	print("Do you want to keep adding items? (y/n)")
	a=input()

print("Sum of Odds numbers: ")
sum_of_odd(r_list)

print("Sum of Even numbers: ")
sum_of_even(r_list)






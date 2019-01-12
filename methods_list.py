colours = ["brown","yellow","blue"]

for x in colours:
	print(x)

print("do you wanna add something (y/n): \n")
ans = input()

if ans == "y":
	
	print("alright mate! : ")
	new_item = input()
	colours.append(new_item)
	print("Now your list is like this!")
	for x in colours:
		
		print(x)

my_favourite_colours = ["cyan","red","black"]
#adding single items, not nesting the entire list into the list
print(" adding a new single item \n")

colours.extend(my_favourite_colours)

for x in colours:
	print(x)

# Now i wanna add an item in the middle of the list

print ("Add in the middle of the list \n")

colours.insert(4, "papaya")

for x in colours:
	print(x)

#remove item (by name)

print("Let's delete an item\n")

print("Which item do you want to remove?: ")

item_remove = input()

colours.remove(item_remove)

print(f"The item removed was {item_remove}\n")

print("Now the list looks like this!\n")
i=0
for x in colours:
	
	print(f"{i}: {x}")
	i+=1

#pop an item by index

print("Maybe you want to pop an item (using index)\n")

answer = int(input())

colours.pop(answer)

i=0

for x in colours:
	
	print(f"{i}: {x}")
	i+=1

print("Check how many times your colour is repeated in the list")

checkeo = input()

print(colours.count(checkeo))

#search colour

print("search this colour:  \n")

ansa = input()

print ("the colour is in the position")
print(colours.index(ansa))

#reverse list

print("let's reverse the list")

colours.reverse()

for x in colours:
	print(x)

#sort list (alphabetically)

print("Let's sort the list alphabetically\n")

colours.sort()

for x in colours:
	print(x)

print ("Now I will clear the list\n")

colours.clear()

for x in colours:
	print(x)


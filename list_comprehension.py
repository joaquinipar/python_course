numbers = [1,2,3,4,5]

double_numbers = [x*2 for x in numbers]

print(double_numbers)

words = ["tree","apple","car"]

capitalised_words = [x.capitalize() for x in words]

print(capitalised_words)

#  [what are you going to do   for  VARIABLE  in  LIST]

numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = [z for z in numbers if z % 2 == 0]

odd_numbers = [y for y in numbers if y%2 != 0]

print(f"New even numbers list created with: {even_numbers}")
print(f"New odd numbers list created with: {odd_numbers}")

rand_number = [1,456,794,49838,989898,785,4843]

rand_new = [num/2 if num %2==0  else num/3 for num in rand_number ]

print(rand_new)

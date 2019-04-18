total=0
def sum_of_kgs (*kilos): # this allows to have indefinite parameters

	for weight in kilos:

		global total
		total += weight
	return total

print(sum_of_kgs(1,5,22,4,5 )) #37



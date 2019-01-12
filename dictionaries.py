Movie = {
		"name": "Back to the Future",
		 "year":1985,
		 "On_Screen":False
		 }

Music = dict(Album_Name="Revolution Radio",Artist="Green Day",year=2016)

print(Movie)
print(Music)

# be careful with "" and ''            here
#                                       |
answer_print = f"The movie is {Movie['name']} , released in {Movie['year']}"

print(answer_print)

for x in Movie.values():

	print(x)

for key,value in Movie.items():

	print(f"{key} : {value}")

# is (X) key in Dictionary?

print("Cast" is Movie)
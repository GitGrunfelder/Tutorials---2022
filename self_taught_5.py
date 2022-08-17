#Ch. 5 pg. 85

#List
fav_artists = ["Korn", "Nirvana", "Gorillaz"]
print(fav_artists)
print("_________________________________________________________________")
#Tuple
coordinates = [(50.433, 67.99), (69.00023, 123.56000)]
print(coordinates)
print("_________________________________________________________________")
#Dictionary - key/value pairs
my_traits = {"height":"5ft 11in", "favorite color":"green", "favorite programming language":"python"}
print(my_traits)
print("_________________________________________________________________")
print("Nice to meet you!")

#Prompts user for a question they would like to know the answer to, from list of choices. converts to lower
question = input("What would you like to know about me? (height, favorite color, favorite programming language) ").lower()
#while answer isn't q for quit, runs loop
while question != "q":
    #if question matches a key in my dictionary, prints that keys value and prompts for another question.
    if question in my_traits:
        print(my_traits[question])
        question = input("What would you like to know about me? (height, favorite color, favorite programming language) ").lower()
    #Otherwise, throws error and asks for another question.
    else:
        print("Please enter a valid choice")
        question = input("What would you like to know about me? (height, favorite color, favorite programming language) ").lower()

#Keys can have lists as values.
artist_song = {
    "Korn":
    ["Freak on a Leash", "Here to Stay", "Somebody Someone"],
    "Nirvana":
    ["In Bloom", "Come as you are", "Lithium"],
    "Gorillaz":
    ["Clint Eastwood", "Feel Good Inc", "Dirty Harry"]
}
#Prints artist and several songs I enjoy by them.
print(artist_song["Nirvana"])

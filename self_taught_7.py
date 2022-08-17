#Ch 7 pg. 114

#Print each item in list
list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in list:
    print(i)

#Print all numbers from 25 to 50
for i in range(25,51):
    print(i)

#Print each item from first problem and their indexes
list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
index = 0
for i in list:
    print(i + "[{}]".format(index))
    index+=1

#Create infinite loop where user guesses a number, if it is in list, they win. Q to quit.
numbers = ["1", "5", "42", "69", "77", "99"]
guess = input("Guess a number up to 100 (q to quit) ")
while guess != 'q':
    if guess in numbers:
        print("Congratulations! You guessed the number! Keep going!")
        guess = input("Guess a number up to 100 (q to quit) ")
    else:
        print("Sorry, that wasn't the number. Try again!")
        guess = input("Guess a number up to 100 (q to quit) ")
print("Goodbye!")

#multiply all numbers in two lists, and make a third list from result
list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
list_3 = []

#for each number in the first list
for i in list_1:
    #for each number in the second list
    for j in list_2:
        #multiply one i by each of the j's one at a time, and append to the third empty list. 
        list_3.append(i * j)
#once the i object has been multiplied by each j, move to next i.
print(list_3)
    

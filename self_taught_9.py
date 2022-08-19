import csv

# write user input into a file, save and close.
user_answer = input("What is your favorite color? ")
with open("example.txt", "w+") as f:
    f.write(user_answer)
    
# Find a file on your computer and print it out.
with open("example.txt", "r") as f: # Open text as readable
    print(f.read()) # Print what is read from variable of opened file.
    

#Take a list of lists, open a csv file as f, convert it into a csv object via .writer function. Put file to be converted as well as a delimiter (where you want to separate items). Then use a for loop to iterate through each item in the list, and print a row for each item in list. 
list1 = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("example.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in list1:
        w.writerow(i)

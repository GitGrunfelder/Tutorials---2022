# Ch 6 pg. 101

# Print each letter in this string
str = "Camus"
for i in str:
    print(i)

# Format some user input into a prewritten statement.
resp1 = input("Name a form of writing: ")
resp2 = input("Name someone you might send that writing to: ")
print("Yesterday I wrote a {}. I sent it to {}!".format(resp1, resp2))

# This problem calls to use the capitalize function in order to turn this string from 'aldous Huxley' to 'Aldous Huxley'...this doesn't quite work as intended, as the first letter becomes capitalized while the rest go lowercase. In the answer solution, the author uses the title() function, which doesn't solve the issue either, because way more capitalization issues occur. 
str = "aldous Huxley was born in 1894."

# My solution is to take the str at the index where the letter that needs to be capitalized occurs, replace it with the capital, and concatenate it to the rest of the str. 
print(str[0].replace("a","A") + str[1:])

# Take this string and return a list with each question as an entry.
str = "Where now? Who now? When now?"
str_list = []
str_list = str.split("? ")
str_list[0] = str_list[0] + "?"
str_list[1] = str_list[1] + "?"
print(str_list)

# Take a list and turn it into a string.
list = ["The", "fox", "jumped", "over", "the", "fence", "."]
# create a str variable that is the list from beginning to last item(not including), joined together by ' ', with a period concatenated at the end.
str = (" ".join(list[:-1])) + list[-1]
print(str)

# Replace 's' with '$'
str = "A screaming comes across the sky."
print(str.replace("s", "$"))

# Find first instance of a char, print the index of the first instance
str = "Hemingway"
print(str.find("m"))

# print a dialogue that include quotes
print('Print every character in the string "Camus"')

# Create "three three three" using concatenation, then multiplication.
print("three" + " three" + " three")
print(("three "* 3).strip())#strip() removes final trailing space

# slice off everything after the comma
str = "It was a bright cold day in April, and the clocks were striking thirteen."
print(str[0:33])


print("This is the first challenge.") #Page 11

print("This is the start of the second set of challenges.")#Page 44
print("Print 3 statements")
print("This is number 3.")

num = int(input("Pick a number: "))
if num < 10:
    print("Small number")
else:
    print("Bigger number (10 or greater)")
    
num = int(input("Pick another number: "))
if num <= 10:
    print("0 - 10")
elif num <= 25:
    print("11 - 25")
else:
    print("Larger than 25")
    
num1 = int(input("Enter a number you'd like to divide: "))
num2 = int(input("How much would you like to divide that by? "))
result = num1 / num2
remainder = num1 % num2
if remainder > 0:
    print(num1, "divided by", num2,"equals:",result,". That expression had a remainder of:",remainder)
else:
    print(num1, "divided by", num2,"equals:",result,". There was no remainder")
    
age = int(input("How old are you? "))
if age <= 10:
    print("You're a little kid!")
elif age <= 25:
    print("Youth, such a great time!")
else:
    print("Rotting corpse. Basically dead.")#End Ch.3 challenges.
    




print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's get started.")
score = 0


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is graphics processing unit.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is random access memory.")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is power supply unit.")

print("Your final score is: " + str(score) + ".")
print("You got " + str((score / 4) * 100) + "% of the answers correct.")
print("Good game!")
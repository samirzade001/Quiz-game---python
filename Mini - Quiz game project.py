# Samir zade 
# @samirzade002

print("(--------------- Welcome to computer quiz!!----------------)")
User_asking = input("Do you want to play? ")

if User_asking.lower() != "yes":
    print("Ok, thank you for playing :)")
    quit()

print("Let's start :) ")
score = 0
answer = input("121 divided by 11 is ")
if answer == '11' or answer.lower() == "eleven":
    print("Correct answer :)")
    score += 1
else:print("Incorrect :(")


print()
answer = input("What is next prime no. after 7? ")
if answer == '11' or answer.lower() == "eleven":
    print("Correct answer :)")
    score += 1
else:print("Incorrect :(")


print()
answer = input("How many months are in one year? ")
if answer == '12' or answer.lower() == "twelve":
    print("Correct answer :)")
    score += 1
else:print("Incorrect :(")


print()
answer = input("50 multiply of 8 is ")
if answer == '400' or answer.lower() == "four hundred":
    print("Correct answer :)")
    score += 1
else:print("Incorrect :(")


print()
answer = input("17 plus 15 = ")
if answer == '32' or answer.lower() == "thirty two":
    print("Correct answer :)")
    score += 1
else:print("Incorrect :(")

print("\n(---------------hey game is over!!---------------)")

print(f"\nyou got correct {score} out of 5 \nyou got " +str((score/5)*100) + "%.")

print("\nKeep growing, keep hustling! :) ")
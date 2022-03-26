#samir zade
#samirzade001

name = input("Enter your name player: ")  #Taking user name as player
print(f"(--------------- Welcome {name} to computer quiz!!----------------)")
User_asking = input(f"{name}, Do you want to play? ")  #Asking user for it's playing intrest or not
 
if User_asking.lower() != "yes":  #if user not intrested in playing
    print("Ok, thank you!! :)")  
    quit()

print("Let's start :) ")  
score = 0  #storing the score of user for showing it's score of wining
answer = input("\n121 divided by 11 is ")
if answer == '11' or answer.lower() == "eleven":
    print(f"Correct answer {name}:)")
    score += 1  #incrementing the score as it's sees to be correct
else:print(f"{name}, Incorrect :(")


print()
answer = input("What is next prime no. after 7? ")
if answer == '11' or answer.lower() == "eleven":
    print(f"Correct answer {name}:)")
    score += 1  #incrementing the score as it's sees to be correct
else:print(f"{name}, Incorrect :(")


print()
answer = input("How many months are in one year? ")
if answer == '12' or answer.lower() == "twelve":
    print(f"Correct answer {name}:)")
    score += 1  #incrementing the score as it's sees to be correct
else:print(f"{name}, Incorrect :(")


print()
answer = input("50 multiply of 8 is ")
if answer == '400' or answer.lower() == "four hundred":
    print(f"Correct answer {name}:)")
    score += 1  #incrementing the score as it's sees to be correct
else:print(f"{name}, Incorrect :(")


print()
answer = input("17 plus 15 = ")
if answer == '32' or answer.lower() == "thirty two":
    print(f"Correct answer {name}:)")
    score += 1  #incrementing the score as it's sees to be correct
else:print(f"{name}, Incorrect :(")

print("\n(---------------hey game is over!!---------------)")

#printing the score and percentage as the user corrected the answer
print(f"\n{name}, you got correct {score} out of 5 \nyou got " +str((score/5)*100) + "%.")
print(f"\n{name} Keep growing, keep hustling! :) ")
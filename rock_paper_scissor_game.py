import random  #importing random for randomly change the numbers !

user_win = 0            #storing user win times in user_win
computer_win = 0        #storing computer win times in computer_win
options = ["rock","paper","scissor"]   #storing the rock, paper, scissor in options for easy procedding


name = input("Enter your name player: ") #Taking user name as player
print(f"Welcome {name} to rock - paper - scissor game !!")

#checking the while is True or Not !!
while True:

#Taking user input for procedding the game
    user_input = input("Enter rock/paper/scissor or 'q' for quite : ").lower()
    if user_input == 'q':
        break

    if user_input not in options:  #If user input invalid text !
        print("Enter the valid input!\n")
        continue

    random_number = random.randint(0, 2)  #randoming the number for make game more exited

    computer_pick = options[random_number]   #initialized for computer picking the random number
    print("computer pick",computer_pick +'.')

    if user_input == "rock" and computer_pick == "scissor":  #rock vs scissor = rock win
        print(f"{name},You win!\n")
        user_win += 1 #incrementing the user win score

    elif user_input == "paper" and computer_pick == "rock": #paper vs rock = paper win
        print(f"{name},You win!\n")
        user_win += 1 #incrementing the user win score

    elif user_input == "scissor" and computer_pick == "paper": #scissor vs paper = scissor win
        print(f"{name},You win!\n")
        user_win += 1  #incrementing the user win score

    else:
        print("You lost!\n")  #if computer win so user lost !
        computer_win += 1 #incrementing the computer win score
print()
print(f"{name},You win {user_win} times and computer win {computer_win} times.")

#showing what is diffrence between user_win and computer_win
if computer_win > user_win:print("Hence,You lost the game by",computer_win-user_win,f"\n\nTry again next time {name}!")
elif computer_win == user_win: print("Match is Tie! :) \n\nYou can restart the game!!")
else: print("Hence, You win the game by",user_win-computer_win,f"\n\nKeep it up {name}!!")  
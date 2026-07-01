import random

def game_menu():
    print("You have three choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Display Wins/Loss")
    print("5 : Exit")

def computer_side_logic():

    computer_choices={1:"Rock",
                      2:"Paper",
                      3:"Scissor"}
    
    computer_select=random.randint(1,3)

    return computer_select

def user_choice_validation(user_choice):
    if user_choice in range(1,6):
        return "Valid"
    else:
        return "Invalid choice.\nPlease enter a integer from menu."

def game_logic(user_choice,computer_select):

    win=0
    loss=0
    draw=0
    total=0
    while True:

        



    


    








# computer_choice={1:"Rock",
#       2:"Paper",
#       3:"Scissor"}


# win=0
# loss=0
# while True:

#     computer=random.randint(1,3)

    
#     user_choice=int(input("Enter your choice :"))

#     if computer-user_choice == 0:
#         print(f"This game is a draw.\nYou selected {computer_choice[user_choice]} computer selected {computer_choice[computer]}.")
#     elif (computer - user_choice) % 3 !=1:
#         print(f"You win.\nYou chose {computer_choice[user_choice]} computer chose {computer_choice[computer]}.")
#         win+=1
#     elif (computer - user_choice) % 3 ==1:
#         print(f"You Lose.\nYou chose {computer_choice[user_choice]} computer chose {computer_choice[computer]}.")
#         loss+=1
#     elif user_choice==4:
#         print(f"Wins:{win}\nLosses:{loss}")
#     elif user_choice==5:
#         break
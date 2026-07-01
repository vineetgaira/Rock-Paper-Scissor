import random

def display_menu():
    print("Here are your choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Display score")
    print("5 : Exit")

def get_user_choice():

    user_choice=int(input("Enter your choice :")) 
    if user_choice in range(1,6):
        return user_choice
    else:
        return "Please enter a valid choice. Choose a number from the given menu."

user_choice = get_user_choice()

def get_computer_choice():
    
    computer=random.randint(1,3)

    return computer

computer_choice = get_computer_choice()

def decide_winner(user_choice,computer_choice):
    
    if computer_choice - user_choice ==0:
        return "It's a draw."
    elif (computer_choice-user_choice) % 3 != 1:
        return  f"You Win.\nComputer chose {computer_choice} You chose {user_choice}."
    elif (computer_choice()-user_choice()) % 3 == 1:
        return  f"You Lose.\nComputer chose {computer_choice} You chose {user_choice}."
    
def display_score():
    pass
    
def main():
    pass

main()

        


    


    









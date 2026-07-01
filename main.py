import random

def display_menu():
    print("Here are your choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Display score")
    print("5 : Exit")

def get_user_choice(user_choice):

    user_choice=int(input("Enter your choice :")) 
    if user_choice in range(1,6):
        print("Valid.")
    else:
        print("Please enter a valid choice from the given menu.")
    
    return user_choice

def get_computer_choice():
    
    computer=random.randint(1,3)

    return computer
    

def decide_winner():
    
    if get_computer_choice()-get_user_choice()==0:
        return "It's a draw."
    elif (get_computer_choice()-get_user_choice()) % 3 != 1:
        return  f"You Win.\nComputer chose {get_computer_choice()} You chose {get_user_choice()}."
    elif (get_computer_choice()-get_user_choice()) % 3 == 1:
        return  f"You Lose.\nComputer chose {get_computer_choice()} You chose {get_user_choice()}."
    
def display_score():
    pass
    
def main():
    pass
    

        


    


    









import random

def display_menu():
    print("Here are your choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Exit")

def get_user_choice():

    user_choice=int(input("Enter your choice :")) 
    if user_choice in range(1,5):
        return user_choice
    print("Please enter a valid choice. Choose a number from the given menu.")
    

def get_computer_choice():
    
    computer=random.randint(1,3)

    return computer


def decide_winner(user,computer):
    computer_choices={1:"Rock",
                      2:"Paper",
                      3:"Scissor"}
    
    if computer - user ==0:
        return "It's a draw."
    elif (computer-user) % 3 != 1:
        return  f"You Win.\nComputer chose {computer_choices[computer]} You chose {computer_choices[user]}."
    elif (computer-user) % 3 == 1:
        return  f"You Lose.\nComputer chose {computer_choices[computer]} You chose {computer_choices[user]}."
    
def update_score():
    pass
    
def play_game():
    while True:

        player_choice=get_user_choice()
        comp_choice=get_computer_choice()
        if player_choice==4:
            print("Thanks for playing.Exiting....")
            break
        result=decide_winner(player_choice,comp_choice)

        print(result)

if __name__=="__main__":
    play_game()



        





        


    


    









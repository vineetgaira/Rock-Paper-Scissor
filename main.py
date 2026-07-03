import random
MOVE_NAMES={1:"Rock",
            2:"Paper",
            3:"Scissor"}

GREEN = "\033[32m"
BLUE = "\033[34m"
RED = " \033[31m"
RESET = "\033[0m"


def display_menu():
    print(f"{GREEN}....Welcome! to Rock, Paper, Scissors....\n"
    "Here are your choices.\n"
    "1 : Rock\n"
    "2 : Paper\n"
    "3 : Scissor\n"
    "4 : Exit")

def get_user_choice():

    valid_choices={1,2,3,4}
    while True:
        try:
            user_choice=int(input(f"Enter your choice :"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please enter a valid choice. LOOK AT THE MENU!")
        except ValueError:
            print(f"Please enter a valid choice. LOOK AT THE MENU!{RESET}")
            
def get_computer_choice():
    
    computer=random.randint(1,3)
    return computer

def decide_winner(user,computer):

    if computer - user ==0:
        return 0
    elif (computer-user) % 3 != 1:
        return  1
    elif (computer-user) % 3 == 1:
        return  -1
    
    
def update_score(result,score_tracker,user,computer):

    if result==0:
        score_tracker["Draw"]+=1
        print(f"{BLUE}Both chose {MOVE_NAMES[user]}.")
    elif result==1:
        score_tracker["User"]+=1
        print(f"You Win!\nYou : {MOVE_NAMES[user]} || Computer : {MOVE_NAMES[computer]}{RESET}")
    else:
        score_tracker["Computer"]+=1
        print(f"{RED}You Lose!\nYou : {MOVE_NAMES[user]}|| Computer :{MOVE_NAMES[computer]}.{RESET}")

    print(f"{BLUE}Scores...\n"
          f"You : {score_tracker["User"]}\n"
          f"Computer : {score_tracker["Computer"]}\n"
          f"Draws: {score_tracker["Draw"]}{RESET}"

    )
 
def play_game():
    
    scores={"User":0,"Computer":0,"Draw":0}
    while True:
        display_menu() 
        player_choice=get_user_choice()
        if player_choice==4:
            print(f"{BLUE}Thanks for playing.\nFinal Results:")
            print(
                f"You : {scores["User"]} || Computer : {scores["Computer"]} || Draws : {scores["Draw"]}{RESET}"
            )
            break
        comp_choice=get_computer_choice()
        round_result=decide_winner(player_choice,comp_choice)
        update_score(round_result,scores,player_choice,comp_choice)

if __name__=="__main__":
    play_game()





    




        





        


    


    









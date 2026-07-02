import random
MOVE_NAMES={1:"Rock",
            2:"Paper",
            3:"Scissor"}

def display_menu():
    print("....Welcome! to Rock, Paper, Scissors....")
    print("Here are your choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Exit")

def get_user_choice():

    valid_choices={1,2,3,4}
    while True:
        try:
            user_choice=int(input("Enter your choice :"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please enter a valid choice. LOOK AT THE MENU!")
        except ValueError:
            print("Please enter a valid choice. LOOK AT THE MENU!")
            
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
        print(f"Both chose {MOVE_NAMES[user]}.")
    elif result==1:
        score_tracker["User"]+=1
        print(f"You Win!\n.You : {MOVE_NAMES[user]} || Computer : {MOVE_NAMES[computer]}")
    else:
        score_tracker["Computer"]+=1
        print(f"You Lose!\n.You : {MOVE_NAMES[user]}|| Computer :{MOVE_NAMES[computer]}.")

    print("Scores...\n"
          f"You : {score_tracker["User"]}\n"
          f"Computer : {score_tracker["Computer"]}\n"
          f"Draws: {score_tracker["Draw"]}"

    )
 
def play_game():
    
    scores={"User":0,"Computer":0,"Draw":0}
    while True:
        display_menu() 
        player_choice=get_user_choice()
        if player_choice==4:
            print("Thanks for playing.\nFinal Results:")
            print(
                f"You : {scores["User"]} || Computer : {scores["Computer"]} || Draws : {scores["Draw"]}"
            )
            break
        comp_choice=get_computer_choice()
        round_result=decide_winner(player_choice,comp_choice)
        update_score(round_result,scores,player_choice,comp_choice)

if __name__=="__main__":
    play_game()





    




        





        


    


    









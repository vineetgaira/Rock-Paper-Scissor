import random

def display_menu():
    print("....Welcome! to Rock, Paper, Scissors....")
    print("Here are your choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Exit")

def get_user_choice():

    user_choice=int(input("Enter your choice :"))
    valid_choices={1,2,3,4}
    try:
        if user_choice in valid_choices:
            return user_choice
    except:       
        if type(user_choice)==str:
            print( "Please enter a valid integer from menu.")
        elif user_choice>4 or user_choice<1:
            print("Please enter a integer between 1 and 4.")
    
            
def get_computer_choice():
    
    computer=random.randint(1,3)

    return computer


def decide_winner(user,computer):

    
    if computer - user ==0:
        return "Draw."
    elif (computer-user) % 3 != 1:
        return  f"You Win."
    elif (computer-user) % 3 == 1:
        return  f"You Lose"
    
def update_score(result,score_tracker,user,computer):
    computer_choices={1:"Rock",
                      2:"Paper",
                      3:"Scissor"}

    if result=="Draw.":
        score_tracker["Draw"]+=1
        print(f"Both chose {computer_choices[user]}.")
    elif result=="You Win.":
        score_tracker["User"]+=1
        print(f"You Win!\n.You : {computer_choices[user]} || Computer : {computer_choices[computer]}")
    else:
        score_tracker["Computer"]+=1
        print(f"You Lose!\n.You : {computer_choices[user]}|| Computer : {computer_choices[computer]}.")

    print("Scores...\n"
          f"You : {score_tracker["User"]}\n"
          f"Computer : {score_tracker["Computer"]}\n"
          f"Draws: {score_tracker["Draw"]}"

    )
 
def play_game():
    
    display_menu() 
    scores={"User":0,"Computer":0,"Draw":0}
    while True:


        player_choice=get_user_choice()
        comp_choice=get_computer_choice()
        if player_choice==4:
            print("Thanks for playing.\nFinal Results:")
            print(
                f"You : {scores["User"]} || Computer : {scores["Computer"]} || Draws : {scores["Draw"]}"
            )
            break
        round_result=decide_winner(player_choice,comp_choice)
        update_score(round_result,scores,player_choice,comp_choice)

    

if __name__=="__main__":
    play_game()



        





        


    


    









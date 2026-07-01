''' So it's pretty much simple.
if Rock-Paper: Paper Wins
Paper-Scissor: Scissor Wins
Scissor-Rock-Rock Wins'''

# Now what I can do is I can assign them a number
# Rock : 1
# Paper : 2
# Scissor: 3
import random

cc={1:"Rock",
      2:"Paper",
      3:"Scissor"}

revcc={"Rock":1,
      "Paper":2,
      "Scissor":2}

computer=random.randint(1,3)

x=revcc[cc[computer]]



win=0
loss=0
while True:

    print("You have three choices.")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Display Wins/Loss")
    print("5 : Exit")
    
    user_choice=int(input("Enter your choice :"))

    if user_choice-x==0:
        print(f"This game is a draw.\nYou selected {cc[user_choice]} computer selected {cc[computer]}.")
    elif x-user_choice== -1 or 2:
        print(f"You win.\nYou chose {cc[user_choice]} computer chose {cc[computer]}.")
        win+=1
    elif user_choice-x== -1 or 2:
        print(f"You Lose.\nYou chose {cc[user_choice]} computer chose {cc[computer]}.")
        loss+=1
    elif user_choice==4:
        print(f"Wins:{win}\nLosses:{loss}")
    elif user_choice==5:
        break
    








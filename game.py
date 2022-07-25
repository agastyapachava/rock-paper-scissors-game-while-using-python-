import random

user1_action = input("enter a choice(rock ,paper,scissors):")
possible_actions =["rock","paper","scissors"]
#user2_action = random.choice(possible_actions)
user2_action = input("enter a chioce(rock,paper,scissors):")
print(f"\nYou chose {user1_action}, user2 chose {user2_action}.\n")
if user1_action == user2_action:
    print(f"both players selected {user1_action}.It,s a tie!")
elif user1_action == "rock":
  if  user2_action == "scissors":
      print ("rock smashes scissors ! you  win !")
  else: 
    print("paper cover rock! you lose.")
elif user1_action == "paper":
    if user2_action == "rock":
        print("paper covers rock ! You win!")
    else :
        print("scissors cuts paper ! you lose.")
elif user1_action == "scissors":
    if user2_action == "paper":
        print("scissors cut paper ! You win !")
    else:
        print("rock smashes scissors! You lose.")
        

        
    

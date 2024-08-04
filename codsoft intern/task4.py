#Rock-Paper-Scissors Game

'''
-1 for rock
0 for paper
1 for scissors
'''

import random    

def game():
    print("Welcome! to Rock-Paper-Scissors Game.")

    choices = {-1 : "rock" , 0 : "paper" , 1 : "scissors"}
    userdic = {"rock" : -1 , "paper" : 0 , "scissors" : 1}
    your_score = 0               
    computer_score = 0

    while True:
        computer = random.choice(list(choices.keys()))     #computer randomly choose any one 

        user = input("Enter your choice (rock / paper / scissors) : ")

        if user not in userdic :
            print("Invalid choice!")
            continue
        
        your = userdic[user]

        print(f"Computer : {choices[computer]} and User : {choices[your]}")

        if (computer == your):
            print("It's a tie.")
        else:
            if(computer == -1 and your == 1):
                print("You lose")
                computer_score += 1
            elif(computer == -1 and your == 0):
                print("You win")
                your_score += 1
            elif(computer == 0 and your == 1):
                print("You win")
                your_score += 1
            elif(computer == 0 and your == -1):
                print("You lose")
                computer_score += 1
            elif(computer == 1 and your == 0):
                print("You lose")
                computer_score += 1
            elif(computer == 1 and your == -1):
                print("You win")
                your_score += 1
                
        play_again = input("Do you want to play again? (yes/no): ")

        if play_again == "no" :
            break                        #if user do not want to play again then print final scores
    print(f"Final scores are : \nYour score {your_score} and Computer score {computer_score}")
    print("Thanks for playing Rock-Paper-Scissors Game!") 
game()
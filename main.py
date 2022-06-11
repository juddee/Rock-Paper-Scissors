import random



def computer_move():
    n=1
    for i in range(n):
       result = random.randint(0,2)

    if result == 0:
        response ='R'
        return response
    elif result == 1:
        response ='P'
        return response
    elif result == 2:
        response ='S'
        return response

    

def check_players_move(users_move,ai_move):
    # check if user choose Rock and Ai choose Scissors
    if users_move == 'R' and ai_move == 'S':
        result = "User wins... Rock Crushes Scissors. AI lose (Scissor)"
        return result
    
    # check if AI choose Rock and User choose Scissors
    elif users_move == 'S' and ai_move == 'R':
        result = "AI wins... Rock Crushes Scissors. You lose (Scissors)"
        return result
    
    # check if user choose Paper and Ai choose Rock
    elif users_move == 'P' and ai_move == 'R':
        result = "User wins... Paper covers Rock. AI lose (Rock)"
        return result  

    # check if AI choose Paper and User choose Rock 
    elif users_move == 'R' and ai_move == 'P':
        result = "AI wins... Paper covers Rock. You lose (Rock)"
        return result
    
    # check if user choose Scissors and Ai choose Paper
    elif users_move == 'S' and ai_move == 'P':
        result = "User wins... Scissors Cuts Paper . AI lose (Paper)"
        return result
    
    # check if AI choose Scissors and User choose Paper
    elif users_move == 'P' and ai_move == 'S':
        result ="AI wins... Scissors Cuts Paper . You lose (Paper)"
        return result 
    # check if user_move is same as ai_move
    elif users_move == ai_move:
        result = 'Draw ...' 
        return result





# Welcome message
print("[Rock-Paper-Scissors]")
print("Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors.")

# instructions for user to select their move
print("Select option")
print("R for rock")
print("P for paper")
print("S for scissors")

while True:
    # take user input move
    user_move = input("Choose your Move(R/P/S): ")
    ai_move = computer_move()
    # check if user input is in our option move
    if user_move.upper() in ('R', 'P', 'S'):

        # check_palyers_move
        result = check_players_move(user_move.upper(),ai_move)
        print(result)

        # break while loop if user choose to not play again
        next_choice = input("Do you want to play again?  (yes/no): ")
        if next_choice == "no":
            break
        elif next_choice=='yes':
            continue
        else:
            print("Invaliid input! Type (yes/no): next time ")
            break
    else:
        print("Enter a valid respond (R/P/S): ")



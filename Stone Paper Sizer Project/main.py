from ai_module import get_computer_choice, user_history
from game_logic import check_winner
from score import update_score, show_score

while True:
    user = input("Enter stone/paper/scissors or exit: ").lower()
    
    if user == "exit":
        break
    
    computer = get_computer_choice()
    print("Computer:", computer)
    
    user_history.append(user)
    
    winner = check_winner(user, computer)
    
    if winner == "draw":
        print("Draw!")
    elif winner == "user":
        print("You Win!")
    else:
        print("Computer Wins!")
    
    update_score(winner)
    show_score()
user_score = 0
computer_score = 0

def update_score(winner):
    global user_score, computer_score
    
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

def show_score():
    print(f"User: {user_score} | Computer: {computer_score}")
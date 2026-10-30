import random
from utils import choices

user_history = []

def get_computer_choice():
    if not user_history:
        return random.choice(choices)
    
    # simple AI: counter most used move
    most_used = max(set(user_history), key=user_history.count)
    
    if most_used == "stone":
        return "paper"
    elif most_used == "paper":
        return "scissors"
    else:
        return "stone"
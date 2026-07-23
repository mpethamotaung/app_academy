"""
Title: The Challenge: “The High-Score Tracker Game”
Description: Build an interactive program that continuously asks an arcade player for their game
score.
"""

# 1. Start with intentional infite loop using while True:

while True:
    user_input = input("Enter your 'score' or 'stop' to end game session: ").strip().lower()

    # if input is a string
    if user_input == "stop":
        print("Game session ended!")
        break

    try:
        score = int(user_input)
    except ValueError:
        print("Please enter a valid number or 'stop' ")
        continue

    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")
    

    

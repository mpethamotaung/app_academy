# Combining loops with decision making
# A guessing game

secret_word = "python"

while True:
    guess = input("Gues the programming language we are using: ").lower()

    if guess == secret_word:
        print("You guessed the correct lanaguage !!!")
        break #keyword to escape a loop
    else:
        print("Try Again")

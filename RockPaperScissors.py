import random

while True:
    guess = ["Rock", "Paper", "Scissors"]
    player = input("Rock, Paper, Scissors, SHOOT!: ")
    player = player.lower()
    guessed = random.choice(guess)
    guessed = guessed.lower()
    print(guessed)
    if player == "rock" and guessed == "paper":
        print("You Lost!")
        print("Paper wraps Rock")
        
    if player == "rock" and  guessed == "scissors":
        print("You Won!")
        print("Rock smashes Scissors")
        
    if player == guessed:
        print("Draw")
        
    if player == "scissors" and guessed == "paper":
        print("You Won!")
        print("Scissors cuts paper")
        
    if player == "scissors" and  guessed == "rock":
        print("You Lost!")
        print("Rock smashes Scissors")
        
    if player == "paper" and  guessed == "scissors":
        print("You Lost!")
        print("Scissors cuts paper")

    if player == "paper" and  guessed == "rock":
        print("You Won!")
        print("Paper wraps Rock")

    # if player == "scissors" or "rock" and guessed == "scissors" or "rock":
    #     print("Rock smashes Scissors")

    # if player == "scissors" or "paper" and guessed == "scissors" or "paper":
    #     print("Scissors cuts paper")

    # if player == "rock" or "paper" and guessed == "rock" or "paper":
    #     print("Paper wraps Rock")
        
    PlayAgain = input("Play Again: YES/NO? ")
    if PlayAgain.lower() != "yes" :
        break


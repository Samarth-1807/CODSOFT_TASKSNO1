import random

print("========================================")
print("     ROCK - PAPER - SCISSORS GAME")
print("========================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"\n----------- ROUND {round_number} -----------")
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1-3): ")

    # Convert number choice into rock, paper, or scissors
    if user_choice == "1":
        user_move = "rock"
    elif user_choice == "2":
        user_move = "paper"
    elif user_choice == "3":
        user_move = "scissors"
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    # Computer randomly selects a choice
    computer_move = random.choice(choices)

    print("\nYour choice      :", user_move)
    print("Computer's choice:", computer_move)

    # Determine the winner
    if user_move == computer_move:
        print("Result: It's a TIE!")

    elif (
        (user_move == "rock" and computer_move == "scissors")
        or (user_move == "paper" and computer_move == "rock")
        or (user_move == "scissors" and computer_move == "paper")
    ):
        print("Result: YOU WIN!")
        user_score += 1

    else:
        print("Result: COMPUTER WINS!")
        computer_score += 1

    # Display score
    print("\n----------- SCORE -----------")
    print("Your score     :", user_score)
    print("Computer score :", computer_score)

    # Ask whether the user wants another round
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

    round_number += 1

print("\n========================================")
print("             FINAL SCORE")
print("========================================")
print("Your score     :", user_score)
print("Computer score :", computer_score)

if user_score > computer_score:
    print("Overall Result: YOU WIN!")
elif computer_score > user_score:
    print("Overall Result: COMPUTER WINS!")
else:
    print("Overall Result: IT'S A TIE!")

print("========================================")
print("       THANK YOU FOR PLAYING!")
print("========================================")
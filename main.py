from random import randint

comp_score = 0
usr_score = 0

while comp_score < 3 and usr_score < 3:
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    ran_num = randint(1, 3)
    computer = None
    player = input("Make your move: ").lower()
    if ran_num == 1:
        computer = "rock"
    elif ran_num == 2:
        computer = "paper"
    elif ran_num == 3:
        computer = "scissors"

    print("Computer is playing: ", computer)

    if computer == player:
        print("it's a tie, no one scores!")
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif computer == "rock" and player == "scissors":
        print("Computer wins!")
        comp_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif computer == "scissors" and player == "paper":
        print("Computer wins!")
        comp_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif computer == "paper" and player == "rock":
        print("Computer wins!")
        comp_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        usr_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif player == "scissors" and computer == "paper":
        print("You win!")
        usr_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    elif player == "paper" and computer == "rock":
        print("You win!")
        usr_score += 1
        print(f"Current score: computer = {comp_score}, you = {usr_score}")
    else:
        print("something went wrong")





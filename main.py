import random

print("Rock...")
print("Paper...")
print("Scissors...")

ran_num = random.randint(1, 3)

computer= None
player = input("Make your move: ").lower()

if ran_num == 1:
    computer = "rock"
elif ran_num == 2:
    computer = "paper"
elif ran_num == 3:
    computer = "scissors"

print("Computer is playing: ", computer)

if computer == player:
    print("it's a tie!")
elif computer == "rock" and player == "scissors":
    print("Computer wins!")
elif computer == "scissors" and player == "paper":
    print("Computer wins!")
elif computer == "paper" and player == "rock":
    print("Computer wins!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
else:
    print("something went wrong")





import random

print("Rock...")
print("Paper...")
print("Scissors...")

ran_num = random.randint(1, 3)

player_one = None
player_two = input("Make your move: ")

print(ran_num)

if ran_num == 1:
    player_one = "rock"
elif ran_num == 2:
    player_one = "paper"
elif ran_num == 3:
    player_one = "scissors"

print(player_one)

if player_one == player_two:
    print("it's a tie!")
elif player_one == "rock" and player_two == "scissors":
    print("Player one wins")
elif player_one == "scissors" and player_two == "paper":
    print("Player one wins")
elif player_one == "paper" and player_two == "rock":
    print("Player one wins")
elif player_two == "rock" and player_one == "scissors":
    print("Player one wins")
elif player_two == "scissors" and player_one == "paper":
    print("Player one wins")
elif player_two == "paper" and player_one == "rock":
    print("Player one wins")
else:
    print("something went wrong")





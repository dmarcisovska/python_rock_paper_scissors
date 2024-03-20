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
elif ran_num == 1:
    player_one = "paper"
elif ran_num == 1:
    player_one = "scissors"



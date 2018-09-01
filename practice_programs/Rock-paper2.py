
import random
# print("Rock ...")
# print("Paper...")
# print("Scissors...")
player_wins = 0
computer_wins = 0
winning_score = 5
while computer_wins < winning_score and player_wins < winning_score:
    print(f"player score: {player_wins} computer scores: {computer_wins}")
    player = input("player make your move: ").lower()
    if player == 'quit' or player == 'q':
        break
     #computer = input("computer make your move: ")
    rand_num = random.randint(0, 2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    print(f"computer plays {computer}")
    if player == computer:
        print("It is a tie")
    elif player == "rock":
        if computer == "scissors":
            print("player_wins")
            player_wins = player_wins + 1
        else:
            print("computer_wins")
            computer_wins = computer_wins + 1
    elif player == "scissors":
        if computer == "paper":
            print("player_wins")
            player_wins = player_wins + 1
        else:
            print("computer_wins")
            computer_wins = computer_wins + 1
    elif player == "paper":
        if computer == "rock":
            print("player_wins")
            player_wins = player_wins + 1
        else:
            print("computer_wins")
            computer_wins = computer_wins + 1
    else:
        print("Please enter a correct move")
if player_wins > computer_wins:
    print("player won")
elif player_wins == computer_wins:
    print("it is a tie")
else:
    print("computer won")
print(f"Final scores...computer scores {computer_wins}... player scores {player_wins}")

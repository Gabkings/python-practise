import random

random_number = random.randint(1, 10)

while True:
    gues = input('Guess a number btw i and ten ')
    if gues != '':
        gues = int(gues)

        if gues > random_number:
            print("Your guess is to way up")

        elif gues < random_number:
            print("Your guess is to lower")

        else:
            print("you got the number")
            play_again = input("Press y to play again or n to quit ").lower()
            if play_again == 'y':
                random_number = random.randint(1, 10)
                gues = None
            else:
                print("thanks for playing")
                break
    else:
        print("please enter a number")
print(random_number)

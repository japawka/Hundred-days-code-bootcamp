################### Scope ####################

enemies = 10


def drink_poison(power):
    global enemies  # Tu pobieramy zmienną globalną do funkcji
    return enemies - power


print(drink_poison(5))

print(enemies)


def increase_enemies():
    return enemies + 5


enemies = increase_enemies()

print(enemies)

import random


def guess_game():
    number = random.randint(1, 100)
    print(number)
    print('Welcome to the Number Guessing Game')
    print("I'm thinking about number between 1 and 100.")
    if input("Choose a difficulty. Type'easy' or 'hard': ") == 'easy':
        counter = 10
    else:
        counter = 5
    game_over = False
    while counter > 0 and not game_over:
        print(f"You have {counter} attemps to guess the number")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            counter -= 1
        elif guess < number:
            print("Too low")
            counter -= 1
        else:
            game_over = True
            print('You have guessed the number. You are WINNER')

    if counter == 0:
        print("You have used all attemps. You lost")
    if input("If you want to plasy again type 'y'") == 'y':
        guess_game()


guess_game()

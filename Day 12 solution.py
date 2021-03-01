import random


def check_answer(guess, number, counter):
    if guess > number:
        print("Too high")
        return counter - 1
    elif guess < number:
        print("Too low")
        return counter - 1
    else:
        print('You have guessed the number. You are WINNER')


def guess_game():
    number = random.randint(1, 100)
    print(number)
    print('Welcome to the Number Guessing Game')
    print("I'm thinking about number between 1 and 100.")
    if input("Choose a difficulty. Type'easy' or 'hard': ") == 'easy':
        counter = 10
    else:
        counter = 5
    guess = 0
    while guess != number:
        print(f"You have {counter} attemps to guess the number")
        guess = int(input("Make a guess: "))

        counter = check_answer(guess, number, counter)

        if counter == 0:
            print("You have used all attemps. You lost")
            return
        elif guess != number:
            print("Guess again ")


guess_game()

from game_data import data, logo, vs
import random
import os

score = 0
should_continue = True
result = ''


def compare(choice, remain):
    global score
    global should_continue
    global result
    if choice['follower_count'] > remain['follower_count']:
        should_continue = True
        score += 1
        result = f'You are right. Current score: {score}'
    else:
        result = f'You are wrong. Current score: {score}'
        should_continue = False

    return result


def game():
    print(logo)
    A = random.choice(data)
    while should_continue:

        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        B = random.choice(data)
        if A == B:
            B = random.choice(data)
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice == 'A':
            compare(A, B)
        else:
            compare(B, A)
        os.system('cls')
        print(logo)

        if should_continue:
            A = B
            print(result)
        else:
            print(result)


game()

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
payer = names[random.randint(0, len(names) - 1)]
print(f'{payer} is going to buy the meal today!')


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
position = input("Where do you want to put the treasure? ")
col = int(position[0])
row = int(position[1])
map[row -1][col -1] = 'x'


print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
pictures = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
computer_choice = random.randint(0, 2)
if player_choice not in range(0, 3):
    print("wrong choice, you lost")
    exit()
else:
    print(pictures[player_choice])

print('Computer chose:')
print(pictures[computer_choice])

if player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 1 or player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 0:
    print("You lost")
else:
    print('You win')

import os
clear = lambda: os.system('clear')
bids = {}
add_bids = True
while add_bids:
    key = input('What is your name? ')
    value = int(input("what's your bid? "))
    bids[key] = value
    question = input('Are there more bidders? yes or no? ')
    if question == "no":
        add_bids = False
    else:
        clear()


for key, value in bids.items():
    if value == max(bids.values()):
        print(f'The winner is {key} with a bid of {bids[key]}')

input("press Enter to finish")
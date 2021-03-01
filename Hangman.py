import random
import hangman_art
import hangman_words

lives = 6
chosen_word = random.choice(hangman_words.word_list)
display = []
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display += '_'
print(display)

end_of_game = False

while not end_of_game:
    guess = input('Guess a letter ').lower()
    if guess in display:
        print(f"Letter {guess} was already guessed")
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"Letter {guess} is not in the word")
        lives -= 1


    if lives == 0:
        end_of_game = True
        print('You loose')

    print(f"{''.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win")
    print(hangman_art.stages[lives])

input("press Enter to exit")
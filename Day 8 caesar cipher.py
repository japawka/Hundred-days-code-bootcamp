import hangman_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_amount, direction):
    new_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
        else:
            new_text += letter
    print(f"The {direction}d text is {new_text}")


print(hangman_art.cip_logo)

end_game = False
while not end_game:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    question = input("Type 'yes' to continue or 'no' to quit  ").lower()
    if question == 'no':
        end_game = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, encode_or_decode):
    new_text = ""
    for letter in text_input:
        letter_position = alphabet.index(letter)
        if encode_or_decode == "decode":
            new_text += alphabet[letter_position - shift_amount]
        elif encode_or_decode == "encode":
            if letter_position + shift_amount < len(alphabet):
                new_text += alphabet[letter_position + shift_amount]
            else:
                new_text += alphabet[-(len(alphabet) - letter_position - shift_amount)]
    print(new_text)


caesar(text, shift, direction)
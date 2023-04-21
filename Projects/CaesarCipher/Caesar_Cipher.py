import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, encode_or_decode):
    new_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in text_input:
        if letter in alphabet:
            new_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        else:
            new_text += letter
    result = input(f"{new_text}\nWould you like to encript or decript another message? yes/no\n")
    if result == "yes":
        direction_new = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text_new = input("Type your message:\n").lower()
        shift_new = int(input("Type the shift number:\n"))
        caesar(text_new, shift_new, direction_new)

caesar(text, shift, direction)


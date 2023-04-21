import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, encode_or_decode):
    new_text = ""
    for letter in text_input:
        if encode_or_decode == "decode":
            shift_amount *= -1
        new_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
    print(new_text)


caesar(text, shift, direction)
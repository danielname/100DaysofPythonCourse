alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if alphabet.index(letter) + shift < len(alphabet):
            cipher_text += alphabet[alphabet.index(letter) + shift]
        else:
            cipher_text += alphabet[-(len(alphabet) - alphabet.index(letter) - shift)]
    print(cipher_text)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        plain_text += alphabet[alphabet.index(letter) - shift]
    print(plain_text)

if direction == "encript":
    encrypt(text,shift)
else:
    decrypt(text,shift)
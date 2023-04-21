alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        cipher_text = ""
        for letter in text_input:
            if alphabet.index(letter) + shift_amount < len(alphabet):
                cipher_text += alphabet[alphabet.index(letter) + shift_amount]
            else:
                cipher_text += alphabet[-(len(alphabet) - alphabet.index(letter) - shift_amount)]
        print(cipher_text)
    elif encode_or_decode == "decode":
        plain_text = ""
        for letter in text_input:
            plain_text += alphabet[alphabet.index(letter) - shift_amount]
        print(plain_text)

caesar(text, shift, direction)
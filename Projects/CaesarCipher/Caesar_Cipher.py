import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, encode_or_decode):
    new_text = ""
    for letter in text_input:
        if encode_or_decode == "decode": #there is currently something wrong with decode I think the issue is on line 14
            shift_amount *= -1
        new_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
    result = input(f"{new_text}\nWould you like to encript or decript another message? yes/no\n")
    if result == "yes":
        direction_new = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text_new = input("Type your message:\n").lower()
        shift_new = int(input("Type the shift number:\n"))
        caesar(text_new, shift_new, direction_new)

caesar(text, shift, direction)

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
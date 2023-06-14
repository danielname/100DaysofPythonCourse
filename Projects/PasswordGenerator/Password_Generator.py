import random
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_lower_letters = int(input("Welcome to Password Generator!\nHow many lowercase letters would you like in your password?\n"))
pass_upper_letters = int(input("How many uppercase letters would you like in your password?\n"))
pass_symbols = int(input("How many symbols would you like in your password?\n"))
pass_numbers = int(input("How many numbers would you like in your password?\n"))

lo_letter_list = []
up_letter_list = []
sym_list = []
num_list = []

password_list = []

for letter in range(pass_lower_letters):
    lo_letter_list.append(lower_letters[random.randint(0, len(lower_letters) - 1)])
for letter in range(pass_upper_letters):
    up_letter_list.append(upper_letters[random.randint(0, len(upper_letters) - 1)])
for symbol in range(pass_symbols):
    sym_list.append(symbols[random.randint(0, len(symbols) - 1)])
for symbol in range(pass_numbers):
    num_list.append(numbers[random.randint(0, len(numbers) - 1)])

lists = lo_letter_list
lists.extend(up_letter_list)
lists.extend(sym_list)
lists.extend(num_list)
for char in range(0,pass_numbers + pass_symbols + pass_lower_letters + pass_upper_letters):
    ran_index = random.randint(0,len(lists) - 1)
    password_list.append(lists[ran_index])
    lists.pop(ran_index)
password = "".join(password_list)
print(f"Here is your password: {password}")
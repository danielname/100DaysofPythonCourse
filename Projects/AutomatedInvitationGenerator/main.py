with open("./Letters/starting_letter.txt") as base:
    base_letter = base.read()

with open("./Names/invited_names.txt") as names:
    name_list = names.read()

with open(f"./Output/ReadyToSend/{name_list}", mode="w") as letter:
    letter.write()
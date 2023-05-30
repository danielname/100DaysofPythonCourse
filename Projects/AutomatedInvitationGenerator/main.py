with open("./Letters/starting_letter.txt") as base:
    base_letter = base.readlines()

with open("./Names/invited_names.txt") as names:
    name_list = names.readlines()

first_line = base_letter[0]

for name in name_list:
    name = name.replace("\n", "")
    named_line = first_line.replace("[name]", name)
    new_letter = []
    for line in range(len(base_letter)):
        if line == 0:
            new_letter.append(named_line)
        else:
            new_letter.append(base_letter[line])
    with open(f"./Output/ReadyToSend/{name}", mode="w") as letter:
        letter.writelines(new_letter)
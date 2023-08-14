student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

def create_phonetic():
    in_word = input("What word would you like a phonetic spelling of?\n")
    nato_list = [letter for letter in in_word.upper()]
    nato_word = []
    for letter in nato_list:
        try:
            nato_word.append(nato_dict[letter])
        except KeyError:
            print("Sorry, only letters in the alphabet please")
            nato_word = ""
            create_phonetic()
            break
    print(nato_word)

create_phonetic()

# next to do, make a recursive function on except
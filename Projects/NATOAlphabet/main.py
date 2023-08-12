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

#TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
for (index, row) in nato_data.iterrows():
    nato_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
in_word = input("What word would you like a phonetic spelling of?")
nato_list = [letter for letter in in_word.upper()]
nato_word = []
for letter in nato_list:
    try:
        nato_word.append(nato_dict[letter])
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        nato_word = ""
        break
print(nato_word)

# next to do, make a recursive function on except
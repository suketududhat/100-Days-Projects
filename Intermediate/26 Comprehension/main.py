# student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas as pd

# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv(
    "C:/Users/suk2d/pyproj/Udemy/100-Days-Projects/Intermediate/26 Comprehension/nato_phonetic_alphabet.csv"
)

phonetic_codes = {row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetic_codes)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ")
phonetic_list = [phonetic_codes[letter.upper()] for letter in user_word]
print(phonetic_list)

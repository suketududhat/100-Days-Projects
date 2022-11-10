with open("Intermediate/24 Mail Merge/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()


with open("Intermediate/24 Mail Merge/Input/Letters/starting_letter.txt") as template:
    letter_content = template.read()

for name in name_list:
    stripped_name = name.strip()
    letter = letter_content.replace("[name]", stripped_name)
    with open(
        f"Intermediate/24 Mail Merge/Output/ReadyToSend/{stripped_name}.txt", "w"
    ) as file:
        file.writelines(letter)

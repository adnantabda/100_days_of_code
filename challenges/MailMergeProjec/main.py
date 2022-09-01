"""Mail Merge Project.
Project for Angela Wu's 100 days of code challenges.
"""

# Guests names
with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names_list = invited_names.read().splitlines()  # Save each line as a list

# Model letter
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    salutation = letter.read()  # Letter as a string

# Final letter
for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(salutation.replace("[name]", name))

"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
"""


def abbrev_name(name):
    name = str(name)
    name = name.split()
    first_name = name[0]
    last_name = name[1]
    first_in = first_name[0].upper()
    second_in = last_name[0].upper()
    return f"{first_in}.{second_in}"

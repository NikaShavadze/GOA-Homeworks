"""
Write a function that removes the spaces from the string, then return the resultant string.
"""


def no_space(x):
    x = list(x)
    y = []
    for i in x:
        if i != " ":
            y.append(i)
    y = "".join(y)
    return y

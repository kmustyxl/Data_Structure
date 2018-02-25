def inverse(char):
    if len(char) == 1:
        return char
    else:
        return char[-1] + inverse(char[:-1])

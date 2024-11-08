def longest_word(sen: str) -> str:
    new_str = ""
    for letter in sen:
        if letter.isalpha() or letter.isnumeric():
            new_str += letter
        else:
            new_str += " "

    return max(new_str.split(), key = len)

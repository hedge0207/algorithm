def first_non_repeating_letter(string):
    idx = -1
    lower_string = string.lower()
    for i, char in enumerate(lower_string):
        if lower_string.count(char) == 1:
            idx = i
            break
    if idx == -1:
        return ""
    else:
        return string[idx]

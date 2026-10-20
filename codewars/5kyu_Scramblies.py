def scramble(s1, s2):
    num_char_s1 = {}
    for char in s1:
        if char in num_char_s1:
            num_char_s1[char] += 1
        else:
            num_char_s1[char] = 1

    for char in s2:
        if char not in num_char_s1 or num_char_s1[char] == 0:
            return False
        else:
            num_char_s1[char] -= 1

    return True
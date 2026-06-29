def twoStrings(s1, s2):
    chars = {}
    for char in s1:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in s2:
        if char in chars:
            return "YES"

    return "NO"
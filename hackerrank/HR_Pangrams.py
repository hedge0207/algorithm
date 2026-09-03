def pangrams(s):
    s = s.lower()
    alphabets = set([chr(i) for i in range(97, 123)])
    for char in s:
        if char in alphabets:
            alphabets.remove(char)
    return "pangram" if len(alphabets) == 0 else "not pangram"
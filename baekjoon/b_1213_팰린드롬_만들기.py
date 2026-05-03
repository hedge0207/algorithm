chars = input()
num_chars = [0]*26

num_odd_chars = 0
for char in chars:
    num_chars[ord(char)-65] += 1
    if num_chars[ord(char)-65] % 2 == 1:
        num_odd_chars += 1
    else:
        num_odd_chars -= 1

if num_odd_chars > 1:
    print("I'm Sorry Hansoo")
else:
    palindrome = ""
    mid_char = ""
    for i in range(26):
        char = chr(i + 65)
        if num_chars[i] % 2 == 1:
            mid_char = char
        palindrome += char * (num_chars[i] // 2)
    print(palindrome + mid_char + palindrome[::-1])
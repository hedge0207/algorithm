from collections import Counter

original_string = input()
n = len(original_string)
counter = Counter(original_string)
num_odd = 0
for char, num in counter.items():
    if num % 2 == 1:
        num_odd += 1

if (n % 2 == 0 and num_odd != 0) or num_odd > 1:
    print("NO SOLUTION")
else:
    palindrome = [""] * n
    st = 0
    ed = n-1
    for char, num in counter.items():
        if num % 2 == 1:
            palindrome[n//2] = char
            num -= 1
        for _ in range(num // 2):
            palindrome[st] = char
            palindrome[ed] = char
            st += 1
            ed -= 1
    print("".join(palindrome))



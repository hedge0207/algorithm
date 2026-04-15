def check_palindrome_type(word):
    l = 0
    r = len(word) - 1
    is_deleted = 0
    last_l, last_r = -1, -1
    while l <= r:
        if word[l] != word[r]:
            if is_deleted:
                break
            is_deleted = 1
            last_l, last_r = l+1, r
        else:
            l += 1
        r -= 1
    else:
        if is_deleted == 0:
            return 0
        else:
            return 1
    if last_l != -1:
        while last_l <= last_r:
            if word[last_l] != word[last_r]:
                break
            last_l += 1
            last_r -= 1
        else:
            return 1
    return 2

n = int(input())
words = [input() for _ in range(n)]
for word in words:
    print(check_palindrome_type(word))
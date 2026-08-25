def camelcase(s):
    ans = 1
    for char in s:
        if char.isupper():
            ans += 1
    return ans
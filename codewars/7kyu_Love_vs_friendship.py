def words_to_marks(s):
    ans = 0
    for char in s:
        ans += ord(char) - 97 + 1
    return ans
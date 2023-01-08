def equalFrequency(word):
    char_cnt = {}
    for char in word:
        if char in char_cnt:
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1

    cnt_lst = list(char_cnt.values())
    for i in range(len(cnt_lst)):
        lst = cnt_lst[:]
        lst[i] -= 1
        if lst[i] == 0:
            lst = lst[:i] + lst[i+1:]

        if max(lst) == min(lst):
            return True

    return False


print(equalFrequency("abc"))

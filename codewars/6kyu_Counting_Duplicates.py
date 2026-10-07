def duplicate_count(text):
    cnt = {}
    ans = 0
    for char in text.lower():
        if char in cnt:
            cnt[char] += 1
            if cnt[char] == 2:
                ans += 1
        else:
            cnt[char] = 1
    return ans
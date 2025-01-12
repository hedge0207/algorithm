def solution(s):
    while len(s) >= 2:
        for idx in range(len(s)-1):
            if s[idx] == s[idx + 1]:
                s = s[:idx] + s[idx+2:]
                break
        else:
            break

    return 1 if not s else -1
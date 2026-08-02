def solution(s):
    answer = []
    last_appearance = {}
    for i in range(len(s)):
        c = s[i]
        if c in last_appearance:
            answer.append(i - last_appearance[c])
        else:
            answer.append(-1)
        last_appearance[c] = i
    return answer
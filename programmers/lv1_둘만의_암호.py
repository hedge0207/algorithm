def solution(s, skip, index):
    skip = set(list(skip))
    answer = ''
    for char in s:
        plus = 0
        move = index
        changed_char = char
        while move != 0:
            plus += 1
            changed_char = chr((ord(changed_char) - ord('a') + 1) % 26 + ord('a'))
            if changed_char not in skip:
                move -= 1

        answer += chr((ord(char) - ord('a') + plus) % 26 + ord('a'))
    return answer
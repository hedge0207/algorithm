# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0
    WORDS = ["aya", "ye", "woo", "ma"]
    for baby_word in babbling:
        idx = 0
        while True:
            if len(baby_word[idx:idx+2]) == 0:
                answer += 1
                break

            if baby_word[idx:idx+3] in WORDS:
                idx += 3
            elif baby_word[idx:idx+2] in WORDS:
                idx += 2
            else:
                break

    return answer
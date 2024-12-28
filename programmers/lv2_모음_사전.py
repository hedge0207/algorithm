def solution(word):
    answer = 0
    chars = ["A", "E", "I", "O", "U"]

    def recursion(k, d, cnt, word, string):
        nonlocal answer
        if k == d:
            return cnt

        for char in chars:
            cnt += 1
            if string + char == word:
                answer = cnt
                return -1
            result = recursion(k + 1, d, cnt, word, string + char)
            if result == -1:
                return -1
            else:
                cnt = result
        return cnt

    recursion(0, 5, 0, word, "")

    return answer
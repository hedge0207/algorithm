def solution(N):
    answer = N
    def recur(cur, fuel):
        nonlocal  answer

        if answer != N:
            return

        if cur < 0:
            return

        if fuel > answer:
            return

        if cur == 0:
            answer = min(answer, fuel)
            return

        if cur % 2 == 0:
            recur(cur // 2, fuel)
        recur(cur-1, fuel + 1)

    recur(N, 0)
    return answer


# best practice
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for i in range(n):
        answer[i] = n - i - 1
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i-idx

        stack.append(i)

    return answer
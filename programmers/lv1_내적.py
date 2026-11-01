def solution(a, b):
    answer = 0
    for num1, num2 in zip(a, b):
        answer += num1 * num2
    return answer
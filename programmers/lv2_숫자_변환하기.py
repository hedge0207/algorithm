def solution(x, y, n):
    answer = -1
    queue = [y]
    cnt = 0
    while queue:
        new_queue = []
        for num in queue:
            if num == x:
                answer = cnt
                new_queue = []
                break
            if num % 3 == 0:
                new_queue.append(num // 3)
            if num % 2 == 0:
                new_queue.append(num // 2)
            if num - n >= x:
                new_queue.append(num - n)
        queue = new_queue
        cnt += 1

    return answer


# print(solution(10, 40, 5))
print(solution(10, 40, 30))
# print(solution(2, 5, 4))

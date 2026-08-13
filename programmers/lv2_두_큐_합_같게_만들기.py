from collections import deque


def solution(queue1, queue2):
    answer = -1
    s1, s2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    if (s1+s2) % 2:
        return answer
    for i in range(len(queue1) * 2):
        if s1 > s2:
            num = queue1.popleft()
            queue2.append(num)
            s1 -= num
            s2 += num
        elif s1 < s2:
            num = queue2.popleft()
            queue1.append(num)
            s1 += num
            s2 -= num
        else:
            answer = i
            break
    return answer
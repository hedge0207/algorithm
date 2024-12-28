from queue import PriorityQueue


def solution(n, k, e):
    pri_queue = PriorityQueue(maxsize=k)
    m = len(e)

    if k >= m:
        return m

    for i in range(k):
        pri_queue.put(e[i])

    sum_ = 0
    for i in range(k, len(e)):
        num_enemy = e[i]

        min_num_enemy = pri_queue.get()
        if min_num_enemy < num_enemy:
            pri_queue.put(num_enemy)
            sum_ += min_num_enemy
        else:
            pri_queue.put(min_num_enemy)
            sum_ += num_enemy

        if sum_ > n:
            return i

    return len(e)
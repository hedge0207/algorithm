from collections import deque

def find_minimum_number_in_slide(n: int, l: int, nums: list[int]):
    queue = deque()
    result = []
    for ed in range(n):
        st = ed - l + 1
        while st >= 0 and queue and queue[0] < st:
            queue.popleft()

        while queue and nums[queue[-1]] >= nums[ed]:
            queue.pop()

        if len(queue) == 0 or nums[queue[0]] <= nums[ed]:
            queue.append(ed)
        result.append(queue[0])

    for i in result:
        print(nums[i], end=" ")


N, L = map(int, input().split())
arr = list(map(int, input().split()))
find_minimum_number_in_slide(N, L, arr)
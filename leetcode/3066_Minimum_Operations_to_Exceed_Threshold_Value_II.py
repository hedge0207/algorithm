from queue import PriorityQueue


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        priority_queue = PriorityQueue()
        for num in nums:
            priority_queue.put(num)

        cnt = 0
        while 1:
            num1 = priority_queue.get()
            if num1 >= k:
                break
            num2 = priority_queue.get()
            priority_queue.put(min(num1, num2)*2 + max(num1, num2))
            cnt += 1
        return cnt
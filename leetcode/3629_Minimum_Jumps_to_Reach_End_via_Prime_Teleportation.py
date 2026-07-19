from collections import defaultdict, deque


class Solution:
    def minJumps(self, nums: list[int]) -> int:
        indices_per_num = defaultdict(list)
        for i in range(len(nums)):
            indices_per_num[nums[i]].append(i)

        product_per_num = {num: {num} for num in nums}
        max_num = max(nums)
        is_prime_number = [1] * (max_num + 1)
        is_prime_number[0] = 0
        is_prime_number[1] = 0

        for i in range(2, max_num + 1):
            if is_prime_number[i] == 0:
                continue
            product = 2
            while i * product <= max_num:
                is_prime_number[i * product] = 0
                if i in indices_per_num and i * product in indices_per_num:
                    product_per_num[i].add(i * product)
                product += 1

        def bfs():
            visited = [0] * len(nums)
            visited[0] = 1
            queue = deque([[0, 0]])
            while queue:
                node, dist = queue.popleft()
                if node == len(nums) - 1:
                    return dist
                if node > 0 and visited[node-1] == 0:
                    visited[node-1] = 1
                    queue.append([node-1, dist+1])
                if node < len(nums)-1 and visited[node+1] == 0:
                    visited[node+1] = 1
                    queue.append([node+1, dist+1])

                if is_prime_number[nums[node]]:
                    for neighbor_num in product_per_num[nums[node]]:
                        for neighbor in indices_per_num[neighbor_num]:
                            if visited[neighbor] == 0:
                                visited[neighbor] = 1
                                queue.append([neighbor, dist+1])
                        indices_per_num[neighbor_num] = []

        return bfs()
class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort(reverse=True)
        num_apples = sum(apple)
        total_cap = 0
        ans = 0
        for i in range(len(capacity)):
            total_cap += capacity[i]
            if total_cap >= num_apples:
                ans = i+1
                break
        return ans
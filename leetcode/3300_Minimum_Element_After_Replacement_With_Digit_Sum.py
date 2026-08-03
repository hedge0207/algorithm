class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = float("inf")
        for num in nums:
            ans = min(ans, sum(list(map(int, str(num)))))
        return ans

# best_practice
class Solution:
    def minElement(self, nums: list[int]) -> int:
        l = []
        for i in nums:
            v = self.calculate(i)
            l.append(v)
        return min(l)

    def calculate(self,num):
        su = 0
        while num > 0:
            t = num % 10
            su = su + t
            num = num // 10
        return su
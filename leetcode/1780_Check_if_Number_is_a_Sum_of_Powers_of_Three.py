import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans = False
        limit = math.ceil(math.log(n, 3))
        def recur(sum_, d):
            nonlocal ans
            if sum_ > n:
                return
            if sum_ == n:
                ans = True
            if d > limit:
                return

            recur(sum_ + 3**d, d+1)
            recur(sum_, d+1)
        recur(0,0)
        return ans

# best_practice
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            q, r=divmod(n,3)
            if r==2:
                return False
            n=q
        return True
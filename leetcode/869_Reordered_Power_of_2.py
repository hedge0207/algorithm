class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_two = set()
        power_of_two.add(1)
        num = 2
        while num <= 10 ** 9:
            power_of_two.add(num)
            num *= 2

        str_num = str(n)
        length = len(str_num)
        visited = [0] * length
        ans = False
        def combination_number(combination):
            nonlocal ans
            if len(combination) == length:
                if int(combination) in power_of_two:
                    ans = True
                return
            for i in range(length):
                if len(combination) == 0 and str_num[i] == "0":
                    continue
                if visited[i] == 1:
                    continue
                visited[i] = 1
                combination_number(combination + str_num[i])
                visited[i] = 0

        combination_number("")
        return ans


# best practice
# n이 2의 제곱과 구성 숫자만 동일하면 된다.
from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))
        length = len(str(n))
        for power in range(31):
            p = str(1 << power)
            if len(p) == length and Counter(p) == n_count:
                return True
        return False
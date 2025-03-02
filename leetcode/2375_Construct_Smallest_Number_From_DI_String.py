class Solution:
    def smallestNumber(self, pattern: str) -> str:
        max_value = 987654321
        used_nums = [0] * 10
        n = len(pattern)
        result = max_value

        def recur(k, num):
            nonlocal result

            if n+1 == len(num):
                result = min(result, int(num))
                return

            direction = pattern[k]
            if direction == "I":
                for i in range(int(num[-1]), 10):
                    if used_nums[i] == 1:
                        continue

                    used_nums[i] = 1
                    recur(k+1, num + str(i))
                    used_nums[i] = 0
            else:
                for i in range(1, int(num[-1])+1):
                    if used_nums[i] == 1:
                        continue

                    used_nums[i] = 1
                    recur(k+1, num + str(i))
                    used_nums[i] = 0

        for i in range(1, 10):
            used_nums[i] = 1
            recur(0, str(i))
            used_nums[i] = 0
            if result < max_value:
                break

        return str(result)
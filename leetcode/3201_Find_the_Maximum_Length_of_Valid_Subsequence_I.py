class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        num_odd = 0
        num_even = 0
        is_odd_lst = []
        for num in nums:
            if num % 2 == 0:
                num_even += 1
                is_odd_lst.append(0)
            else:
                num_odd += 1
                is_odd_lst.append(1)

        cnt = 0
        for flag in range(2):
            tcnt = 0
            for is_odd in is_odd_lst:
                if is_odd == flag:
                    flag = 0 if flag else 1
                    tcnt += 1
            cnt = max(tcnt, cnt)
        return max(num_odd, num_even, cnt)

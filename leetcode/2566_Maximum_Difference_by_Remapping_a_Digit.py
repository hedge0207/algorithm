class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = list(map(int, str(num)))
        num_change_to_nine = 9
        for num in nums:
            if num != 9:
                num_change_to_nine = num
                break
        num_to_change_zero = nums[0]

        changed_max_nums = []
        changed_min_nums = []
        for num in nums:
            max_num = num
            if num == num_change_to_nine:
                max_num = 9
            changed_max_nums.append(str(max_num))

            min_num = num
            if num == num_to_change_zero:
                min_num = 0
            changed_min_nums.append(str(min_num))

        return int("".join(changed_max_nums)) - int("".join(changed_min_nums))
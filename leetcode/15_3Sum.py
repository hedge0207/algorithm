def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        st = i + 1
        ed = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while st < ed:
            if st-1 > i and nums[st] == nums[st - 1]:
                st += 1
                continue

            if ed < len(nums) - 1 and nums[ed] == nums[ed + 1]:
                ed -= 1
                continue

            sum_ = nums[i] + nums[st] + nums[ed]
            if sum_ == 0:
                arr = [nums[i], nums[st], nums[ed]]
                result.append(arr)
                ed -= 1
                st += 1
            elif sum_ > 0:
                ed -= 1
            else:
                st += 1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))

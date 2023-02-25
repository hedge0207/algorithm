def arrayPairSum(nums):
    n = len(nums)
    nums.sort(reverse=True)
    ans = 0
    for i in range(1, n, 2):
        ans += nums[i]
    return ans


print(arrayPairSum([1,4,3,2]))

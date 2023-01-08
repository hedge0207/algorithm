def removeDuplicates(nums):
    cnt = 0
    N = len(nums)
    for slower in range(N-1):
        if nums[slower] == nums[slower+1]:
            nums[slower] = 101
            cnt += 1
    nums.sort()
    return N-cnt

# best practice
def removeDuplicates(nums):
    slower = 0
    for faster in range(1, len(nums)):
        if nums[slower] != nums[faster]:
            slower += 1
        nums[slower] = nums[faster]

    return slower + 1


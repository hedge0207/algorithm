def binary_search(nums, num):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r) // 2
        if num == nums[m]:
            return 1
        elif num > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = sorted(list(map(int, input().split())))
    m = int(input())
    nums2 = list(map(int, input().split()))
    for num in nums2:
        print(binary_search(nums1, num))
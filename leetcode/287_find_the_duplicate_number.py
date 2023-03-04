class Solution(object):
    def findDuplicate(self, nums):
        slower = faster = nums[0]
        while True:
            slower = nums[slower]
            faster = nums[nums[faster]]
            if slower == faster:
                break

        pt1 = nums[0]
        pt2 = faster
        while True:
            if pt1 == pt2:
                break
            pt1 = nums[pt1]
            pt2 = nums[pt2]

        return pt1

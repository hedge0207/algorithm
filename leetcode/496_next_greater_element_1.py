from typing import List


class Solution:

    # 모든 경우를 비교하는 풀이
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = {num: -1 for num in nums1}

        for num in nums:
            for i in range(len(nums2) - 1, -1, -1):
                cur_num = nums2[i]

                if cur_num == num:
                    break

                if cur_num > num:
                    nums[num] = cur_num

        return list(nums.values())

    # stack을 사용하는 풀이
    # stack에는 아직 next_gt_elem을 찾지 못 한 숫자들이 쌓이게 된다.
    def get_next_gt_elem_using_stack(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        next_gt_elems = {num: -1 for num in nums1}

        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num < num and next_gt_elems.get(prev_num):
                    next_gt_elems[prev_num] = num
            stack.append(num)

        return list(next_gt_elems.values())
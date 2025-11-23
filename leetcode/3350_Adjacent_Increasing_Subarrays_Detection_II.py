class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> bool:
        cnt = 1
        prev = 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cnt += 1
            else:
                prev = cnt
                cnt = 1
            ans = max(ans, cnt // 2, min(cnt, prev))
        return max(ans, cnt // 2, min(cnt, prev))

"""
[1,2,3,1,2,5,6,7,8]를 엄격히 증가하는 부분 배열로 분할하면 아래와 같다.
[1,2,3] / [1,2] / [5,6,7,8]
결국 이 문제는 이 세 부분 배열 사이의 길이의 최솟값과 한 부분 배열 내의 길이의 최댓값 중 최댓값을 찾으면 된다.
한 부분 배열 내에서의 최댓값은 "부분 배열의 길이 // 2"이다.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# 풀이2. 투 포인터를 활용한 스왑(정석)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
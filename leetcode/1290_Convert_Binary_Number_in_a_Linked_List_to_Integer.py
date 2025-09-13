from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bits = ""
        node = head
        while node:
            bits += str(node.val)
            node = node.next

        ans = 0
        for i in range(len(bits)):
            if bits[i] == "1":
                ans += 2**(len(bits)-1-i)
        return ans
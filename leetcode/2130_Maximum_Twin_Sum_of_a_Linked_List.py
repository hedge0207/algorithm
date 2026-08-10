from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = [head]
        while 1:
            node = nodes[-1].next
            if node is None:
                break
            nodes.append(node)

        ans = 0
        for i in range(len(nodes)//2):
            ans = max(ans, nodes[i].val + nodes[len(nodes)-1-i].val)
        return ans
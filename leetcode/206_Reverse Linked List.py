# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_cur = None
        cur = head
        while True:
            if cur is None:
                break

            next_node = cur.next
            cur.next = new_cur
            new_cur = cur
            cur = next_node

        return new_cur

# 재귀 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev=None):
            if node is None:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

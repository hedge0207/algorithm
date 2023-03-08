# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import builtins


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            next_ = cur.next
            if cur == head:
                head = next_
            tmp = next_.next
            if tmp:
                if next_.next.next:
                    cur.next = next_.next.next
                else:
                    cur.next = next_.next
            else:
                cur.next = None

            next_.next = cur
            cur = tmp

        return head

# best practice
def swapPairs(head):
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        next_ = head.next
        head.next = next_.next
        next_.next = head

        prev.next  = next_

        head = head.next
        prev = prev.next.next

    return root.next

# recursion
def swapPairs(head):
    if head and head.next:
        next_ = head.next
        head.next = swapPairs(next_.next)
        next_.next = head
        return next_
    return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        cur = start = head
        before = prev = None
        cnt = 0
        while True:
            cnt += 1
            next_ = cur.next

            if cnt > left:
                cur.next = prev

            if cnt == right:
                if before:
                    before.next = cur
                start.next = next_
                if left == 1:
                    head = cur
                break

            if cnt == left:
                before = prev
                start = cur

            prev = cur
            cur = next_

        return head
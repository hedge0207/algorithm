# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        for node in [l1, l2]:
            cnt = 0
            while node:
                sum_ += node.val * 10 ** cnt
                cnt += 1
                node = node.next
        sum_ = str(sum_)

        head = prev = None
        for i in range(len(sum_) - 1, -1, -1):
            num = int(sum_[i])
            node = ListNode(num)
            if i == len(sum_) - 1:
                head = node

            if prev:
                prev.next = node

            prev = node

        return head


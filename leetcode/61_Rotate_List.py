from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        n = 1
        node = head
        while node.next:
            n += 1
            node = node.next
        node.next = head

        node = head
        before = None
        for i in range(n-(k%n)):
            before = node
            node = node.next
        new_head = node
        if before is not None:
            before.next = None
        return new_head
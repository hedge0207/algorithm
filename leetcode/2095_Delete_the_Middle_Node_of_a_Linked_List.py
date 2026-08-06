from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        nodes = [head]
        while 1:
            node = nodes[-1].next
            if node is None:
                break
            nodes.append(node)
        idx_to_remove = len(nodes) // 2
        if idx_to_remove == len(nodes)-1:
            nodes[len(nodes)//2-1].next = None
        else:
            nodes[len(nodes) // 2 - 1].next = nodes[len(nodes) // 2 + 1]
        return head



# best practice
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        curr=fast=slow=head
        while fast and fast.next:
            curr=slow
            slow=slow.next
            fast=fast.next.next
        curr.next=slow.next
        return head


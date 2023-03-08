# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even_head = None
        while odd and odd.next:
            even = odd.next
            if even_head is None:
                even_head = even

            if even.next:
                odd.next = even.next
                odd = odd.next
                if even.next.next:
                    even.next = even.next.next
                else:
                    even.next = None
            else:
                break

        if head:
            odd.next = even_head

        return head
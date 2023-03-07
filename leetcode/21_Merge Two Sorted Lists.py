class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_head = cur = ListNode(0)
        non_empty_lst = None
        while 1:
            if list1 is None:
                while list2 is not None:
                    cur.next = list2
                    cur = cur.next
                    list2 = list2.next
                break

            if list2 is None:
                while list1 is not None:
                    cur.next = list1
                    cur = cur.next
                    list1 = list1.next
                break

            if list1.val > list2.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next

        return tmp_head.next


# best practice
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# 재귀 활용
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if (list1 is None) or (list2 is not None and list1.val > list2.val):
        list1, list2 = list2, list1
    if list1 is not None:
        list1.next = self.mergeTwoLists(list1.next, list2)
    return list1
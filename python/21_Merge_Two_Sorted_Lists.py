# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        m = ListNode()
        last = m
        l1 = list1
        l2 = list2
        while l1 and l2 :
            if l1.val <= l2.val:
                last.next =l1
                l1 = l1.next
            else:
                last.next =l2
                l2 = l2.next
            last = last.next
        if l1:
            last.next = l1
        elif l2:
            last.next = l2
        return m.next

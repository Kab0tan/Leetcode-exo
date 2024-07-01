# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head.val
            new = ListNode(curr)
            tail = new
            head = head.next
            while head:
                if head.val != curr:
                    curr = head.val
                    tail.next = ListNode(head.val)
                    tail = tail.next
                head = head.next
            return new
        else:
            return head

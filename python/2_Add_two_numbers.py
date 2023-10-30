# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val+l2.val<10:
            l3 = ListNode(l1.val+l2.val)
            tmp = l3
            l1 = l1.next
            l2 = l2.next
            c=0
        else:
            l3 = ListNode(l1.val+l2.val-10)
            tmp = l3
            l1 = l1.next
            l2 = l2.next
            c=1
        while True:
            if (l1 is None) and (l2 is None):
                break
            if (l1 is None) and (l2 is not None):
                l1= ListNode(0)
            elif (l1 is not None) and (l2 is None):
                l2= ListNode(0)
            if l1.val+l2.val+c < 10:
                tmp.next = ListNode(l1.val+l2.val+c)
                c = 0
            else:
                tmp.next = ListNode(l1.val+l2.val+c-10)
                c = 1
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
            if (l1 is None) and (l2 is not None):
                l1= ListNode(0)
            elif (l1 is not None) and (l2 is None):
                l2= ListNode(0)
            
        if c==1:
            tmp.next = ListNode(1)
            tmp =  tmp.next

        return l3

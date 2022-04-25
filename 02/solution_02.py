# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        a = l1
        b = l2
        dummylist = ListNode(0)
        prev = dummylist
        x = 0
        while a != None and b != None:
            if a.val + b.val + x>9:
                y = a.val + b.val + x - 10
                x = 1
            else:
                y = a.val + b.val + x
                x = 0
            newnode = ListNode(0)
            prev.next = newnode
            newnode.val = y
            prev = newnode
            a = a.next
            b = b.next
        while b != None:
            newnode = ListNode(0)
            prev.next = newnode
            newnode.val = b.val + x
            if newnode.val > 9:
                newnode.val = newnode.val-10
                x=1
            else:
                x=0
            prev = newnode 
            b = b.next
        while a != None:
            newnode = ListNode(0)
            prev.next = newnode
            newnode.val = a.val + x
            if newnode.val > 9:
                newnode.val = newnode.val-10
                x=1
            else:
                x=0
            prev = newnode 
            a = a.next
        if x == 1:
            newnode = ListNode(0)
            prev.next = newnode
            newnode.val = 1
        return dummylist.next
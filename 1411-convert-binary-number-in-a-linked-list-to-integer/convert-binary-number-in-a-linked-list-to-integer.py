# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev=None
        cur=head
        while cur:
            nextt=cur.next
            cur.next=prev
            prev=cur
            cur=nextt
        head=prev
        c=0
        x=0
        while head:
            if head.val:
                c+=(1<<x)
            x+=1
            head=head.next
        return c
        
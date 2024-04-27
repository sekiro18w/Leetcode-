# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        h1 = l1
        h2 = l2
        prev_=0
        dummy = ListNode()
        curr=dummy
        while h1 or h2:
            if not h2 or not h1:
                if not h2:
                    vall=h1.val+prev_
                else:
                    vall=h2.val+prev_   
            else:
                vall=(h1.val+h2.val+prev_)
            prev_=(vall)//10
            curr.next = ListNode(vall%10)
            curr=curr.next
            if h1:
                h1=h1.next
            if h2:
                h2=h2.next

        if prev_:
            curr.next=ListNode(prev_)
        head=dummy.next
        return head
        
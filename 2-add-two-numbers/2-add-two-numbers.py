# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        carry = 0
        
        s = p1.val + p2.val
        p1.val = s%10
        carry = s//10
        
        while p1.next and p2.next:
            s = p1.next.val + p2.next.val + carry
            
            p1.next.val = s%10
            carry = s//10
            
            p1 = p1.next
            p2 = p2.next
            
        if p2.next:
            p1.next = p2.next
        
        
        while p1.next and carry > 0:
            s = p1.next.val + carry
            
            p1.next.val = s%10
            carry = s//10
            
            p1 = p1.next
            
            
        if carry > 0:
            p1.next = ListNode(carry)
            
        return l1
            
            
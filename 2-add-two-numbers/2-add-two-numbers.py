# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         p1 = l1
#         p2 = l2
#         carry = 0
    
#         while p1 or carry:
            
#             s = p1.val + (0 if p2 is None else p2.val) + carry
            
#             p1.val = s%10
#             carry = s//10
            
#             if (p1.next is None):
                
#                 if p2 is None:                              #### L1 was longer & we are at the last node of L1
#                     if carry > 0:
#                         p1.next = ListNode(carry)
#                     break
#                 elif p2 is not None and p2.next is None:    #### L1 & L2 are equal in length & we are at the last Node
#                     if carry > 0:
#                         p1.next = ListNode(carry)
#                     break
#                 else:                                       #### L2 was longer & we are at the last node of L1
#                     #### (p1.next is None) and (p2 is not None) and (p2.next is not None):
#                     p1.next = p2.next
#                     p2.next = None
                
#             p1 = p1.next
#             p2 = None if p2 is None else p2.next
        
#         return l1
                
        
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        carry = 0
        #### Add the values of first two elements
        s = p1.val + p2.val
        p1.val = s%10
        carry = s//10
        
        #### Keep adding values of next nodes until next exists for both
        while p1.next and p2.next:
            s = p1.next.val + p2.next.val + carry
            
            p1.next.val = s%10
            carry = s//10
            
            p1 = p1.next
            p2 = p2.next
        
        #### After above loop, we will have added the first x digits where x = min(m, n)
        #### We will now add the rest to the carry or leave them as is
        
        #### If p1 was longer, we will ocntinue the loop & add carry to each element of p1
        #### If p2 was longer, we will move them to p1 & do the same as above 
        
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
    
############# Time Complexity: O(max(m, n)) #############
## 1. Traverse each list parallelly --> O(max(m, n))

############# Space Complexity: O(1) #############
## 1. No Extra Space
            
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         endPointer = delPointer = head
#         for i in range(n):
#             endPointer = endPointer.next
            
#         if endPointer is None:
#             head = head.next
#             return(head)

#         while endPointer.next is not None:
#             endPointer = endPointer.next
#             delPointer = delPointer.next
        
#         delPointer.next = delPointer.next.next
        
#         return(head)
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #### To remove nth item from the end, we have to pint to the n+1th item from the end
        
        l = r = head
        
        while n >= 0:
            if r is None:
                head = head.next
                return(head)
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return head
        
    
    
############# Time Complexity: O(n) #############
## 1. Iterate through the array ---> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra Space ---> O(1)
            
        
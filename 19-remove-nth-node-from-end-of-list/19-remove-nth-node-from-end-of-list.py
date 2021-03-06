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
        
        #### To remove nth item from the end, we have to point to the n+1 th item from the end. 
        #### So we move right pointer by n times & iterate until r reaches end ( not r reaches NULL )
        #### 1st node from end is last node, & so on 
        l = r = head
        
        for i in range(n):       ### move r n times
            r = r.next
            if r is None:
                head = head.next
                return(head)
        
        while r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return head
    
    
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         #### To remove nth item from the end, we have to point to the n+1 th item from the end. 
#         #### So we move right pointer by n+1 times & iterate until r reaches NULL ( not r reaches end )
#         #### 1st node from end is last node, & so on 
#         l = r = head
        
#         for i in range(n+1):       ### move r n+1 times
#             if r is None:
#                 head = head.next
#                 return(head)
#             r = r.next
            
        
#         while r:
#             l = l.next
#             r = r.next
        
#         l.next = l.next.next
#         return head
    
    
############# Time Complexity: O(n) #############
## 1. Iterate through the array ---> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra Space ---> O(1)
            
        
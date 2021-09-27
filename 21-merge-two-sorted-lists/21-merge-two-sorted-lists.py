# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return(None)
            
        if l1 is None or l2 is None:
            return(l1 if l2 is None else l2)
        
        
        head = itr = ListNode(float('-inf'))
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                itr.next = l1
                l1 = l1.next        
            else:
                itr.next = l2
                l2 = l2.next
            itr = itr.next
            itr.next = None
            
            
        if l1 is not None:
            itr.next = l1
        
        if l2 is not None:
            itr.next =  l2
        
        
        
        return(head.next)
            
                
        
        
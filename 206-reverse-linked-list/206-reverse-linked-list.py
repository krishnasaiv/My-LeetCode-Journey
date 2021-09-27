# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return(None)
        
        from collections import deque
        q = deque()
        
        while head:
            q.append(head)
            itr = head.next
            head.next = None
            head = itr
            
        
        head = itr = q.pop()
        while len(q):
            itr.next = q.pop()
            itr = itr.next
            
        return(head)
            
            
        
        
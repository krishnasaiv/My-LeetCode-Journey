# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head.next is None or head.next.next is None:
            return head
        
        #### Find Middle
        l = r = head
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
            
        middle = l.next
        l.next = None
        
        #### Reverse list from Middle
        prev = None
        cur = middle
        
        while cur:
            nxt = cur.next
            
            cur.next = prev
            
            prev = cur
            cur = nxt
        middle = prev
        
        
        #### Merge Head & Middle
        cur1, cur2 = head, middle
        
        while cur2:
            nxt1 = cur1.next
            nxt2 = cur2.next
            
            cur1.next = cur2
            cur2.next = nxt1
            
            cur1 = nxt1
            cur2 = nxt2
        
        return head
        
        
            
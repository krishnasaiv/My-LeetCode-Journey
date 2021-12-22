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
        l.next = None       # Remove the link between first half & the second half
        
        
        #### Reverse list from Middle
        prev = None
        cur = middle
        while cur:
            nxt = cur.next      # save the location of the next pointer ( the rest of the list ) so that it is not lost
            
            cur.next = prev     # move the next pointer in current node to previous 
            
            prev = cur          # update the prev & cur
            cur = nxt
        middle = prev
        
        
        #### Merge Head & Middle
        cur1, cur2 = head, middle
        while cur2:
            nxt1 = cur1.next    # save the next pointers in each list
            nxt2 = cur2.next
            
            cur1.next = cur2    # Move first element from list2 next to the current node in list1
            cur2.next = nxt1
            
            cur1 = nxt1         # Update Current Node locations in both lists
            cur2 = nxt2

        return head
        
        
            
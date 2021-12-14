# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    ################################################
    ## Method 1: Stack --> O(n), O(n)
    ################################################
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return(None)
        
#         from collections import deque
#         q = deque()
        
#         while head:
#             q.append(head)
#             itr = head.next
#             head.next = None
#             head = itr
            
        
#         head = itr = q.pop()
#         while len(q):
#             itr.next = q.pop()
#             itr = itr.next
            
#         return(head)
    
    ################################################
    ## Method 2: 3 Pointer Iterative --> O(n), O(1)
    ################################################
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev= None
        cur = head        
        while cur:
            ## Save the pointer to the rest of the linkedList
            nxt = cur.next
            
            ## Move the connection from cur->nxt to cur->prev
            cur.next = prev
            
            ## Modify prev, cur pointers
            prev = cur
            cur = nxt
        
        
        return prev
            

    ################################################
    ## Method 3: Recursive --> O(n), O(1)
    ################################################
            
            
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = r = head
        
        while (r.next is not None) and (r.next.next is not None):
            l = l.next
            r = r.next.next
            
        return(l if r.next is None else l.next)
    
############# Time Complexity: O(n) #############
## 1. Iterate two pointers through the list, fast moves n times, slow moves n/2 ties ---> O(n)

############# Space Complexity: O() #############
## 1. NO Extra Space --> O(1)


##### After iteration i, position sof 
#####   l = i
#####   r = 2*i-1 
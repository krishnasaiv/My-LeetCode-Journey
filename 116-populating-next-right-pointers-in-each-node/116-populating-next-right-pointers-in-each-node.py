"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        if not root:
            return None
        
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            prev = None
            for i in range(l):
                n = q.popleft()
                if n.left: 
                    q.append(n.left)
                    
                    if prev is not None:
                        prev.next = n.left
                    prev = n.left
                if n.right:
                    q.append(n.right)
                    
                    prev.next = n.right
                    prev = n.right
                    
        return root
                    
                
        
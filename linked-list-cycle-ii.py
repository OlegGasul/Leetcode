class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        visited = set()
        
        node = head
        while node:
            if node in visited:
                return node
            
            visited.add(node)
            node = node.next
            
        return None
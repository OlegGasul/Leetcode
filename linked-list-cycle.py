class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head) -> bool:
    visited = set()
        
    node = head
    while node:
        if node in visited:
            return True
            
        visited.add(node)
        node = node.next
            
    return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

print(hasCycle(head))
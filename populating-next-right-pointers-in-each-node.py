class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root
    
    queue = [root]
        
    while queue:
        queue.append(None)
            
        newQueue = []
        
        for i in range(len(queue) - 1):
            queue[i].next = queue[i + 1]
            if queue[i].left:
                newQueue.append(queue[i].left)
            if queue[i].right:
                newQueue.append(queue[i].right)
                
        queue = newQueue
            
    return root

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
connect(root)
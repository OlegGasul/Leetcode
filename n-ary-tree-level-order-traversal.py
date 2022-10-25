class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

def levelOrder(root):
    if not root:
        return []
        
    queue = [root]
        
    result = []
        
    while queue:
        newQueue = []
        level = []
            
        for node in queue:
            level.append(node.val)
            if node.children:
                newQueue.extend(node.children)
                
        result.append(level)
            
        queue = newQueue
            
    return result

print(levelOrder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
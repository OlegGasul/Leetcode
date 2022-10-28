class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    result = []
        
    if not root:
        return result
        
    queue = [root]
        
    while queue:
        result.append(queue[-1].val)
            
        newQueue = []
            
        for node in queue:
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
        
    return result

print(rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
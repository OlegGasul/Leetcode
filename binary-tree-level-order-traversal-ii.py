class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    if not root:
        return []
        
    result = []
    queue = [root]
        
    while queue:
        newQueue = []
        level = []
            
        for node in queue:
            level.append(node.val)
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
            
        result.insert(0, level)
    
    return result

print(levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
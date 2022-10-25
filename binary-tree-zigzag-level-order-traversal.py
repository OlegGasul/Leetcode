class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []
        
    queue = [root]
        
    order = True
    result = []
        
    while queue:
        newQueue = []
        level = []
            
        for node in queue:
            if order:
                level.append(node.val)
            else:
                level.insert(0, node.val)
                
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        result.append(level)
        queue = newQueue
            
        order = not order
            
    return result

print(zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
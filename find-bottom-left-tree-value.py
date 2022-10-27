class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root) -> int:
    result = 0
        
    queue = [root]
        
    while queue:
        newQueue = []
            
        result = queue[0].val
            
        for node in queue:
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
            
    return result

print(findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
print(findBottomLeftValue(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))))
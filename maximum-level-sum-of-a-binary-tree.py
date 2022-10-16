class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root) -> int:
    queue = [root]
    result = -1
    
    level = 1
    maxValue = float('-inf')
        
    while queue:
        newQueue = []
        value = 0
            
        for node in queue:
            value += node.val
            
            if node.left:
                newQueue.append(node.left)
                    
            if node.right:
                newQueue.append(node.right)
            
        if value > maxValue:
            result = level
            maxValue = value
            
        queue = newQueue
        level += 1
            
    return result

print(maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))
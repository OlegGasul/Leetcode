class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def printNode(node):
    if node:
        print(node.val)
    else:
        print('None')

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if not cloned:
        return None
        
    targetVal = target.val
        
    def dfs(node):
        if node.val == targetVal:
            return node
            
        if node.left:
            result = dfs(node.left)
            if result:
                return result
                
        if node.right:
            result = dfs(node.right)
            if result:
                return result
                
        return False
        
    result = dfs(cloned)
        
    return result if result else None

printNode(getTargetCopy(
    TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19))),
    TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19))),
    TreeNode(3, TreeNode(6), TreeNode(19))
))
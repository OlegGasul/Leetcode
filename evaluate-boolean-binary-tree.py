class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root) -> bool:
    if not root:
        return False
        
    def dfs(node):
        if not node.left and not node.right:
            return True if node.val == 1 else False
            
        leftValue = dfs(node.left) if node.left else True
        rightValue = dfs(node.right) if node.right else True
            
        if node.val == 2:
            return leftValue or rightValue
        else:
            return leftValue and rightValue
            
    return dfs(root)

print(evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))))
print(evaluateTree(TreeNode(0)))
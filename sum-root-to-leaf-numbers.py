class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root) -> int:
    result = 0
        
    def dfs(node, value):
        nonlocal result
            
        value = value * 10 + node.val
            
        if not node.left and not node.right:
            result += value
        else:
            if node.left:
                dfs(node.left, value)
            if node.right:
                dfs(node.right, value)
                    
    dfs(root, 0)
        
    return result

print(sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
print(sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    result = 0
        
    def dfs(node, maximum):
        nonlocal result
            
        if node.val >= maximum:
            result += 1
            
        maximum = max(maximum, node.val)
        if node.left:
            dfs(node.left, maximum)
        if node.right:
            dfs(node.right, maximum)
                
    dfs(root, float('-inf'))
        
    return result

print(goodNodes(TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))))
print(goodNodes(TreeNode(1)))
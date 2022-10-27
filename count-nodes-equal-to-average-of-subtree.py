class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def averageOfSubtree(root) -> int:
    result = 0
        
    def dfs(node):
        nonlocal result
            
        if not node.left and not node.right:
            result += 1
            return [1, node.val]
            
        leftCount = 0
        leftSum = 0
            
        if node.left:
            leftCount, leftSum = dfs(node.left)
            
        rightCount = 0
        rightSum = 0
            
        if node.right:
            rightCount, rightSum = dfs(node.right)
                
        totalCount = leftCount + 1 + rightCount
        totalSum = leftSum + node.val + rightSum
            
        value = totalSum // totalCount
        if value == node.val:
            result += 1
                
        return [totalCount, totalSum]
                
    dfs(root)
        
    return result

print(averageOfSubtree(TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))))
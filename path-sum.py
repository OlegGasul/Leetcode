class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum: int) -> bool:
    if root == None:
        return False
    
    if root.left == None and root.right == None:
        return root.val == targetSum

    diff = targetSum - root.val
    if root.left != None:
        if hasPathSum(root.left, diff):
            return True
    if root.right != None:
        if hasPathSum(root.right, diff):
            return True

    return False
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(hasPathSum(root, 3))
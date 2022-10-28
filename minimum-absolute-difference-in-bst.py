import bisect

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root) -> int:
    if not root:
        return -1
        
    nums = []
        
    result = float('inf')
        
    def dfs(node):
        nonlocal result
        
        index = bisect.bisect_left(nums, node.val)
        nums.insert(index, node.val)

        if index > 0:
            result = min(result, abs(nums[index] - nums[index - 1]))
        if index < len(nums) - 1:
            result = min(result, abs(nums[index + 1] - nums[index]))
                
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
                
    dfs(root)
                
    return result

print(getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
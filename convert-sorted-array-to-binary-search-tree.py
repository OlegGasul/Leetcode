class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):

    def traverse(nums):
        if len(nums) == 0:
            return None
            
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = traverse(nums[: mid])
        root.right = traverse(nums[mid + 1 : ])

        return root
        
    return traverse(nums)

print(sortedArrayToBST([-10, -3, 0, 5, 9]))
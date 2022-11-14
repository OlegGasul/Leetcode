class TreeNode:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

class NumArray:

    def __init__(self, nums):
        prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        def prepareNode(left, right):
            node = TreeNode(left, right, prefixSum[right] - prefixSum[left - 1])
            
            if left < right:
                middle = left + (right - left) // 2
                node.leftTree = prepareNode(left, middle)
                node.rightTree = prepareNode(middle + 1, right)
            
            return node

        self.root = prepareNode(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def dfs(node):
            if node.left == index and node.right == index:
                node.value = val
                return node.value

            if node.leftTree and index >= node.leftTree.left and index <= node.leftTree.right:
                node.value = dfs(node.leftTree) + (node.rightTree.value if node.rightTree else 0)
            elif node.rightTree and index >= node.rightTree.left and index <= node.rightTree.right:
                node.value = (node.leftTree.value if node.leftTree else 0) + dfs(node.rightTree)

            return node.value

        dfs(self.root)
        
    def sumRange(self, left: int, right: int) -> int:
        
        def dfs(node, left, right):
            if node.left == left and node.right == right:
                return node.value

            result = 0

            if node.leftTree and right <= node.leftTree.right:
                result += dfs(node.leftTree, left, right)
            elif node.rightTree and left >= node.rightTree.left:
                result += dfs(node.rightTree, left, right)
            else:
                result += dfs(node.leftTree, left, min(right, node.leftTree.right))
                result += dfs(node.rightTree, max(left, node.rightTree.left), right)

            return result

        return dfs(self.root, left, right)
        

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))

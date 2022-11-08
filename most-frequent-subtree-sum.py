from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root):
        counter = Counter()

        def dfs(node):
            nonlocal counter

            current = node.val
            
            if not node.left and not node.right:
                counter[current] += 1
                return current

            if node.left:
                current += dfs(node.left)
            if node.right:
                current += dfs(node.right)

            counter[current] += 1

            return current

        dfs(root)

        mostCommon = counter.most_common()
        result = []

        value, minCount = mostCommon.pop(0)
        result.append(value)

        while mostCommon:
            value, count = mostCommon.pop(0)
            if count < minCount:
                break
            
            result.append(value)

        return result

solution = Solution()
print(solution.findFrequentTreeSum(TreeNode(5, TreeNode(2), TreeNode(-3))))
print(solution.findFrequentTreeSum(TreeNode(5, TreeNode(2), TreeNode(-5))))
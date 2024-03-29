from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root, queries):
        depth = defaultdict(int)
        cousins = defaultdict(list)

        def dfs(node, currentDepth):
            if not node:
                return -1

            depth[node.val] = currentDepth
            current = max(dfs(node.left, currentDepth + 1), dfs(node.right, currentDepth + 1)) + 1
            
            cousins[currentDepth].append((current, node.val))
            if len(cousins[currentDepth]) > 2:
                cousins[currentDepth].sort(reverse = True)
                cousins[currentDepth].pop()
            
            return current
        
        dfs(root, 0)

        result = []
        for query in queries:
            currentDepth = depth[query]
            if len(cousins[currentDepth]) == 1:
                result.append(currentDepth - 1)
            elif cousins[currentDepth][0][1] == query:
                result.append(cousins[currentDepth][1][0] + currentDepth)
            else:
                result.append(cousins[currentDepth][0][0] + currentDepth)

        return result

root = TreeNode(1, TreeNode(3, TreeNode(2)), TreeNode(4, TreeNode(6), TreeNode(5, None, TreeNode(7))))
solution = Solution()
assert solution.treeQueries(root, [4]) == [2]
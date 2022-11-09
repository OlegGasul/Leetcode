import bisect

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        result = []

        def bfs(root):
            if not root:
                return
            
            queue = [root]

            while queue:
                newQueue = []

                for node in queue:
                    index = bisect.bisect_left(result, node.val)
                    result.insert(index, node.val)

                    if node.left:
                        newQueue.append(node.left)
                    if node.right:
                        newQueue.append(node.right)

                queue = newQueue

        bfs(root1)
        bfs(root2)

        return result

solution = Solution()
print(solution.getAllElements(TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(1, TreeNode(0), TreeNode(3))))

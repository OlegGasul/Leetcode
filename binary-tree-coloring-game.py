class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root, n: int, x: int) -> bool:

        def calculateNodes(node):
            if not node:
                return 0
            
            result = 1
            
            if node.left:
                result += calculateNodes(node.left)
            if node.right:
                result += calculateNodes(node.right)

            return result

        if root.val == x:
            return calculateNodes(root.left) != calculateNodes(root.right)

        def dfs(node):
            if node.val == x:
                a = calculateNodes(node.left)
                b = calculateNodes(node.right)
                c = n - (a + b + 1)

                return a > b + c or b > a + c or c > a + b

            if node.left:
                result = dfs(node.left)
                if result != None:
                    return result
            if node.right:
                result = dfs(node.right)
                if result != None:
                    return result

            return None

        return dfs(root)

solution = Solution()
print(solution.btreeGameWinningMove(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6), TreeNode(7))), 11, 3))
# The solution is not working on Leetcode, because 0 is set for all values in the tree

import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root) -> int:
    hp = []
    heapq.heapify(hp)
    
    nodeSet = set()

    def dfs(node, parent):
        nodeSet.add(node.val)

        nodes = []
        if parent:
            nodes.append(parent.val)

        if node.left:
            nodes.append(node.left.val)
            dfs(node.left, node)
        if node.right:
            nodes.append(node.right.val)
            dfs(node.right, node)

        heapq.heappush(hp, [-len(nodes), node.val, nodes])
        heapq.heapify(hp)

    dfs(root, None)

    result = 0

    while hp:
        data = heapq.heappop(hp)
        if data[1] in nodeSet:
            for node in data[2]:
                nodeSet.discard(node)

            result += 1

    return result

print(minCameraCover(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))))
print(minCameraCover(TreeNode(1, TreeNode(2), TreeNode(3))))
print(minCameraCover(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))))
print(minCameraCover(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))))
print(minCameraCover(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6))))))))
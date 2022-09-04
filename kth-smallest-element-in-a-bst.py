import heapq

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k: int) -> int:
    queue = []
    heapq.heapify(queue)

    nodes = [root]

    while nodes:
        node = nodes.pop()
        
        heapq.heappush(queue, node.val)
        heapq.heapify(queue)

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return heapq.nsmallest(k, queue)[-1]


print(kthSmallest(TreeNode(2, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))
print(kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3))
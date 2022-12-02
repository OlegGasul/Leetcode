class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k: int):
        nodes = []
        
        node = head
        while node:
            nodes.append(node)
            node = node.next

        nodes[k - 1].val, nodes[- k].val = nodes[- k].val, nodes[k - 1].val

        return head

solution = Solution()
solution.swapNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def dfs(node):
            if not node.next:
                node.val += 1
            else:
                node.val += dfs(node.next)
            
            if node.val == 10:
                node.val = 0
                return 1
            else:
                return 0
        
        return head if dfs(head) == 0 else ListNode(1, head)

solution = Solution()
solution.plusOne(ListNode(1, ListNode(2, ListNode(3))))
solution.plusOne(ListNode(1, ListNode(2, ListNode(9))))
solution.plusOne(ListNode(1, ListNode(2, ListNode(8))))
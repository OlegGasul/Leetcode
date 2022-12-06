class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        if not head:
            return head
        
        tempHead = ListNode()
        tempHead.next = head

        first = tempHead
        stack = []
        node = head

        while node:
            stack.append(node)
            
            if len(stack) == k:
                currentNext = node.next
                while stack:
                    first.next = stack.pop()
                    first = first.next
                first.next = currentNext
                node = currentNext
            else:
                node = node.next

        return tempHead.next

solution = Solution()
solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
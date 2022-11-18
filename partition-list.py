class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x: int):
        less = ListNode(float('-inf'))
        lessHead = less
        
        greater = ListNode(float('-inf'))
        greaterHead = greater

        node = head

        while node:
            if node.val < x:
                less.next = node
                less = less.next
            else:
                greater.next = node
                greater = greater.next

            nextNode = node.next
            node.next = None
            node = nextNode

        if less.val != float('-inf'):
            head = lessHead.next
            if greater.val != float('-inf'):
                less.next = greaterHead.next
        elif greater.val != float('-inf'):
            head = greaterHead.next

        return head

solution = Solution()
solution.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(5)))))))

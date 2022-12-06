class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head):
        if not head or not head.next:
            return head
        
        k = 2
        stack = []
        first = head
        counter = 0
        node = head.next

        while node:
            stack.append(node)
            counter += 1

            if counter == k or not node.next:
                if (k % 2 == 0 and counter == k) or (counter % 2 == 0 and not node.next):
                    currentNext = node.next
                    while stack:
                        first.next = stack.pop()
                        first = first.next
                    first.next = currentNext
                    node = currentNext
                else:
                    stack = []
                    first = node
                    node = node.next

                counter = 0
                k += 1
            else:
                node = node.next

        return head

solution = Solution()
solution.reverseEvenLengthGroups(ListNode(5, ListNode(2, ListNode(6, ListNode(3, ListNode(9, ListNode(1, ListNode(7, ListNode(3, ListNode(8, ListNode(4)))))))))))
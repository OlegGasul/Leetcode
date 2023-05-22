class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        node = head
        for i in range(n):
            node = node.next
        
        left = head
        prev = None

        while node:
            node = node.next
            temp = left
            left = left.next
            prev = temp
        
        if not prev:
            return left.next
        
        prev.next = left.next

        return head

def createListNode(values):
    head = ListNode(values.pop(0))
    node = head

    while values:
        node.next = ListNode(values.pop(0))
        node = node.next
    
    return head

def resolveValues(head):
    values = []
    node = head

    while node:
        values.append(node.val)
        node = node.next
    
    return values

solution = Solution()
assert resolveValues(solution.removeNthFromEnd(createListNode([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert resolveValues(solution.removeNthFromEnd(createListNode([1, 2]), 1)) == [1]
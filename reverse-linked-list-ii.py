class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def createList(values):
    head = ListNode(values.pop(0))

    node = head
    while values:
        node.next = ListNode(values.pop(0))
        node = node.next
    
    return head

def printList(head):
    node = head

    result = []
    while node:
        result.append(node.val)
        node = node.next
    
    print(result)

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head:
            return head
        
        newHead = ListNode(0, head)

        stack = []

        node = head
        prev = newHead

        i = 1
        while node and i < left:
            prev = node
            node = node.next
            i += 1
        
        nextNode = None
        while node and i <= right:
            stack.append(node)
            
            nextNode = node.next
            node = node.next

            i += 1
        
        while stack:
            prev.next = stack.pop()
            prev = prev.next

        prev.next = nextNode

        return newHead.next

solution = Solution()
printList(solution.reverseBetween(createList([1, 2, 3, 4, 5]), 2, 4))
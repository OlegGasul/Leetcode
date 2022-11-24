class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createListNode(values):
    head = ListNode(values.pop(0))
    node = head

    while values:
        node.next = ListNode(values.pop(0))
        node = node.next

    return head

def printListNode(head):
    values = []
    
    while head:
        values.append(head.val)
        head = head.next
    
    print(values)

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        keep = m

        while node:
            keep -= 1
            if not keep:
                skip = n
                skipNode = node.next

                while skipNode and skip:
                    skipNode = skipNode.next
                    skip -= 1
                
                keep = m
                node.next = skipNode
                node = skipNode
            else:
                node = node.next

        return head

solution = Solution()
printListNode(solution.deleteNodes(createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 2, 3))
printListNode(solution.deleteNodes(createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1, 3))
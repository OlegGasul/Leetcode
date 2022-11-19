class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodeA = headA
        nodeB = headB
        visited = set()

        while nodeA or nodeB:
            if nodeA == nodeB:
                return nodeA
            
            if nodeA in visited:
                return nodeA
            elif nodeB in visited:
                return nodeB

            if nodeA:
                visited.add(nodeA)
                nodeA = nodeA.next
            if nodeB:
                visited.add(nodeB)
                nodeB = nodeB.next

        return None

solution = Solution()
intersection = ListNode(3, ListNode(1, ListNode(2)))
headA = ListNode(1, ListNode(2, intersection))
headB = ListNode(1, ListNode(2, intersection))

print(solution.getIntersectionNode(headA, headB))
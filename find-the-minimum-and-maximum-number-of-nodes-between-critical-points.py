class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def createList(nums):
    head = ListNode(nums.pop(0))
    node = head

    while nums:
        node.next = ListNode(nums.pop(0))
        node = node.next

    return head

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = float('inf')
        firstCritical = None
        lastCritical = None
        
        i = 1
        first = None
        second = None
        node = head
        while node:
            if first and second:
                if (first > second and second < node.val) or (first < second and second > node.val):
                    if not firstCritical:
                        firstCritical = i
                    if lastCritical:
                        minDistance = min(minDistance, i - lastCritical)
                    lastCritical = i

            first = second
            second = node.val

            node = node.next
            i += 1

        return [minDistance, lastCritical - firstCritical] if firstCritical and lastCritical and firstCritical < lastCritical else [-1, -1]

solution = Solution()
print(solution.nodesBetweenCriticalPoints(createList([5, 3, 1, 2, 5, 1, 2])))
print(solution.nodesBetweenCriticalPoints(createList([1, 3, 2, 2, 3, 2, 2, 2, 7])))
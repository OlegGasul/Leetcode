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
    def nodesBetweenCriticalPoints(self, head):
        criticals = []
        minDistance = float('inf')
        
        i = 1
        first = None
        second = None
        node = head

        while node:
            if first and second:
                if first > second and second < node.val:
                    criticals.append(i)
                elif first < second and second > node.val:
                    criticals.append(i)
                if len(criticals) > 1:
                    minDistance = min(minDistance, criticals[-1] - criticals[-2])

            first = second
            second = node.val

            node = node.next
            i += 1

        if len(criticals) < 2:
            return [-1, -1]
        else:
            return [minDistance, criticals[-1] - criticals[0]]

solution = Solution()
print(solution.nodesBetweenCriticalPoints(createList([5, 3, 1, 2, 5, 1, 2])))
print(solution.nodesBetweenCriticalPoints(createList([1, 3, 2, 2, 3, 2, 2, 2, 7])))
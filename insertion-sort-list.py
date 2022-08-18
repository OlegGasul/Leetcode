class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printNodes(head):
    print(head.val)
    
    while head.next:
        head = head.next
        print(head.val)
        

def insertElement(nums, value):
    length = len(nums)

    left = 0
    right = length - 1

    while left < right:
        middle = left + (right - left) // 2

        if value > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1

    if value <= nums[left]:
        nums.insert(left, value)
    else:
        nums.insert(right + 1, value)

def makeList(nums):
    root = ListNode(nums[0])
    item = root
    for i in range(1, len(nums)):
        item.next = ListNode(nums[i])
        item = item.next

    return root

def insertionSortList(head):
    nums = [head.val]
    result = []
    while head.next:
        head = head.next
        insertElement(nums, head.val)

    return makeList(nums)

# [4, 2, 1, 3]
# head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
# [-1, 5, 3, 4, 0]
head = ListNode(-1,
    ListNode(5,
        ListNode(3,
            ListNode(4,
                ListNode(0)))))

result = insertionSortList(head)
printNodes(result)
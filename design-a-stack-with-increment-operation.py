class CustomStack:

    def __init__(self, maxSize: int):
        self.nums = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.nums) == self.maxSize:
            print(self.nums)
            return
        
        self.nums.append(x)
        

    def pop(self) -> int:
        if len(self.nums) == 0:
            return -1
        
        return self.nums.pop(len(self.nums) - 1)
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.nums))):
            self.nums[i] += val

customStack = CustomStack(3)    # Stack is Empty []
customStack.push(1)             # stack becomes [1]
customStack.push(2)             # stack becomes [1, 2]
print(customStack.pop())        # return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2)             # stack becomes [1, 2]
customStack.push(3)             # stack becomes [1, 2, 3]
customStack.push(4)             # stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100)   # stack becomes [101, 102, 103]
customStack.increment(2, 100)   # stack becomes [201, 202, 103]
print(customStack.pop())        # return 103 --> Return top of the stack 103, stack becomes [201, 202]
print(customStack.pop())        # return 202 --> Return top of the stack 102, stack becomes [201]
print(customStack.pop())        # return 201 --> Return top of the stack 101, stack becomes []
print(customStack.pop())        # return -1 --> Stack is empty return -1.
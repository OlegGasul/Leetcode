class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return len(self.queue) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
print(stack.pop())
print(stack.empty())
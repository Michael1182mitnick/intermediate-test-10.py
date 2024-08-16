# Implement a stack using two queues.

from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Push the element onto queue2
        self.queue2.append(x)

        # Push all the elements of queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # Remove and return the top element
        if not self.queue1:
            return "Stack is empty"
        return self.queue1.popleft()

    def top(self):
        # Return the top element without removing it
        if not self.queue1:
            return "Stack is empty"
        return self.queue1[0]

    def empty(self):
        # Return whether the stack is empty
        return len(self.queue1) == 0


# Example usage
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.top())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.empty())  # Output: False
print(stack.pop())  # Output: 10
print(stack.empty())  # Output: True

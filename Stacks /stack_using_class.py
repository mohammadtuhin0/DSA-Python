class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# Create a stack 
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print(f"Stack: {myStack.stack}")
print(f"Pop: {myStack.pop()}")
print(f"Stack after Pop: {myStack.stack}")
print(f"Peek: {myStack.peek()}")
print(f"isEmpty: {myStack.isEmpty()}")
print(f"Size: {myStack.size()}")
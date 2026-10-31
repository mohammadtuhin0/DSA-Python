x = [5, 6, 2, 9, 3, 8, 4, 2]

stack = []

# push
stack.append('A')
stack.append('B')
stack.append('C')
print(f"Stack: {stack}")

# peek 
topElement = stack[-1]
print(f"Peek : {topElement}")

# pop 
poppedElement = stack.pop()
print(f"Pop: {poppedElement}")

# Stack After Pop
print(f"Stack after Pop: {stack}")

#isEmpty
isEmpty = not bool(stack)
print(f"isEmpty: {isEmpty}")

# size 
print(f"Size: {len(stack)}")
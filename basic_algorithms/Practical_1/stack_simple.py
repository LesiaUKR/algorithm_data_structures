import time

# Через список
start = time.time()
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack: ', stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
stack.append('d')
print(stack.pop())
print(stack.pop())

print(time.time() - start)
print('\nStack after elements are popped:', stack)





# Через LifoQueue
from queue import LifoQueue
start = time.time()
# Initializing a stack
stack = LifoQueue(maxsize=4)

stack.put('a')
stack.put('b')
stack.put('c')

print("Initial stack: ", stack.queue)

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
stack.put('d')
print(stack.get())
print(stack.get())

print(time.time() - start)
print("\nStack after elements are popped: ", stack.queue)





# Через зв'язний список
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    # Get the current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head  # Make the new node point to the current head
        self.head = node  # Update the head to be the new node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


# Driver Code
stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(f"Initial stack: {stack}")
print('\nElements popped from the stack')
print(stack.pop())
print(stack.pop())
stack.push("d")
print(stack.pop())
print(stack.pop())

print(time.time() - start)
print(f"\nStack after elements are popped: {stack}")



# Stack we know for LIFO = Last In First Out

# Initialized the linked list head by this
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        new_node = Node(value)

        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            popped_node = self.head
            self.head = self.head.next
            self.size -= 1
            return popped_node.value

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print()

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Linked List: ", end="")
my_stack.traverse()

print("Pop:", my_stack.pop())
print("LinkedList after pop: ", end="")
my_stack.traverse()

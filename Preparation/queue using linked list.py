class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        self.size -= 1

        if self.front is None:
            self.rear = None
        return temp.value

    def traverse(self):
        current_node = self.front
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next

        print()



my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.traverse()

my_queue.dequeue()
my_queue.traverse()
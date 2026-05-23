# singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def insert_at_end(self, data):
        new_data = Node(data)

        if not self.head:
            self.head = new_data
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_data

    def delete(self, value):
        temp = self.head

        if temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp:
            prev = temp
            temp = temp.next
            if temp.data == value:
                prev.next = temp.next
                break


    def search(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next


data = LinkedList()

data.insert_at_end(1)
data.insert_at_end(2)
data.insert_at_end(3)
data.search()

print("\n")
data.delete(1)
data.search()


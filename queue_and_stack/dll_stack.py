from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Increase the size of the storage
        self.size += 1
        # Add item to the head of the stack
        self.storage.add_to_head(value)

    def pop(self):
        pass

    def len(self):
        pass

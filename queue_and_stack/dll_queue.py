from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Instantiate doubly_link
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Increase the size of the storage
        self.size += 1
        # Add item for the storage 
        self.storage.add_to_tail(value)
        

    def dequeue(self):
        # Check if the storage is empty
        if self.len() > 0:
             # Decrease the size of the storage when item is removed
            self.size -= 1
            # get value of item at the head to be removed
            value = self.storage.head.value
            # Remove the item from the head
            self.storage.remove_from_head()
            return value
        

    def len(self):
        pass

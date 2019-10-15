from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.storage = DoublyLinkedList()
        """
            once the cache is holding the max number of entries,
            if a new entry is to be inserted,
            another pre-existing entry needs to be evicted from the cache.
            Once you access an item/get, it moves to the front of the list
            The least recently used is gonna be at the tail of the list
            The data structure to use is an hashtable for fast look ups
            Advantages of a doubly linked list is that you can remove and add an item in constant time
            # PROBLEMS
            1. How do we know where the least recently used item is.
            2. How do we remove items quickly
        """

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        current_node = ListNode(value)
        # when you get an item, set the key to 1
        # Move the item to the head of the list
        if (self.storage == None):
            # Storage is empty, return -1
            return -1
        self.storage.move_to_front(current_node)
        self.key = 1
        return current_node.value
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        node = value

        if node == None:
            



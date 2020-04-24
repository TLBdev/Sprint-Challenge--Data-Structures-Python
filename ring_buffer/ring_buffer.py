from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0
    def append(self, item):
        
        if self.size < self.capacity:
            self.size += 1
            self.storage.add_to_tail(item)
        else:
            
            self.current.value = item
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
        if self.size == 1:
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

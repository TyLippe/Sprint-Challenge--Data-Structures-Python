from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if not at capacity we need to add to ring
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            #set current to head item
            self.current = self.storage.head
        #if we are at capacity we need to overwrite oldest data
        elif self.capacity == self.storage.length:
            #head is the oldest in a ring
            removed = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if removed == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        #add first value in
        first_item = self.current
        list_buffer_contents.append(first_item.value)
        #if we have a next we will give it a var
        if first_item.next:
            next_item = first_item.next
        else:
            next_item = self.storage.head
        #loop through DLL using while self.next
        #in loop we will continue to append items
        while next_item is not first_item:
            list_buffer_contents.append(next_item.value)
            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

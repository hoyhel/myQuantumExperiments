class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Node:
    def __init__(self, value):
        # Create two instance attributes: value and next (the pointer)
        self.val = value
        self._next = None

    def value(self):
        # Return the value of node object: self.val
        return self.val

    def next(self): 
        # Return the value of self.next (the pointer)
        return self._next


class LinkedList:
    def __init__(self, values=None):
        # Create a head instance attribute and set it to None
        self._head = None
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        # Iterate over the list
        current_node = self._head
        while current_node is not None:
            yield current_node.value()
            current_node = current_node.next()

    def __len__(self):
        counter = 0
        current_node = self._head
        while current_node is not None:
            counter += 1
            current_node = current_node.next()
        return counter

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        current_head = self._head
        self._head = self._head.next()
        return current_head.val

    def reversed(self):
        new = LinkedList()
        for value in self:
            new.push(value)
        return new
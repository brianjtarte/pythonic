
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    pass

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.value
        else:
            if self.top is None:
                raise InvalidOperationError("Method not allowed on empty collection")

    def reverse_string(self, string):
        rev_string = ''
        for letter in string:
            self.push(letter)
            current = self.top
        while current:
            rev_string += current.value
            current = current.next
        return rev_string










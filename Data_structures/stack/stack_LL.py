class Node:
    def __init__(self, data, next_node=None):
        self.value = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        self.head = Node(data, self.head)

    def remove(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        temp = self.head
        self.head = self.head.next
        del temp
    
    def show_top(self):
        if self.head is None:
            raise IndexError("no top for empty stack")
        return self.head.value
    
    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        return count

class LLStack:
    def __init__(self, data):
        self.head = LinkedList()

    def push(self, data):
        self.head.append(data)

    def pop(self):
        self.head.remove()
    
    def top(self):
        return self.head.show_top()

    def size(self):
        return self.head.size()
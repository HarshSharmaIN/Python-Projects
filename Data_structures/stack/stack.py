class Stack:
    """
    This is a stack using the list container from python
    Attributes: stack instance created during the creation of the object

    Methods:
    1. push: pushes the new data onto the top of the stack
    2. pop: pops the data out from the top of the stack
    3. top: returns the data at the top of the stack
    4. size: returns the size of the stack at that moment
    """
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

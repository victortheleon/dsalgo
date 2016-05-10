__author__ = "Manish Kumar"
__email__ = "victortheleon@gmail.com"

class Stack(object):
    """A very simple class to represent a stack data structure,its 
    corresponding methods and properties. This class is implemented
    with list. Feel free to fork and improve it"""
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return self.stack == []
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)


def reverse(line):
    st = Stack()
    for char in line:
        st.push(char)
    rev = ""
    while not st.is_empty():
        rev += st.pop()
    return rev

print reverse("manish")
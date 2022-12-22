
class Node:  # Node or Link
    """
    """
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return self.value


class ChainedList:

    def __init__(self, *args):
        if len(args) > 0:
            self.data = Node(args[0])
            current_node = self.data
            for value in args[1:]:
                current_node.next = Node(value)
                current_node = current_node.next
        else:
            self.data = Node()

    def add_element(self, value):
        pass

    def remove_element



class Stack:

    def __init__(self):
        self.items = 0
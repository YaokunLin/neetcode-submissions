class Node():
    def __init__(self, value=-1, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node

        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        first_node = self.head.next
        new_node = Node(value)
        
        self.head.next = new_node
        new_node.prev = self.head

        new_node.next = first_node
        first_node.prev = new_node
        
    def pop(self) -> int:
        if self.isEmpty(): return -1
        last_node = self.tail.prev
        last_node_vale = last_node.value
        second_last_node = last_node.prev

        second_last_node.next = self.tail
        self.tail.prev = second_last_node

        return last_node_vale

    def popleft(self) -> int:
        if self.isEmpty(): return -1
        first_node = self.head.next
        first_node_value = first_node.value
        second_node = first_node.next

        self.head.next = second_node
        second_node.prev = self.head

        return first_node_value
        


        

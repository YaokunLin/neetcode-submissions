class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head
        counter = 0
        while cur:
            if counter == index + 1:
                return cur.val
            counter += 1
            cur = cur.next
        return -1
        
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        counter = 0
        while cur and counter < index:
            counter += 1
            cur = cur.next
            if not cur: return False
        
        # cur is the node BEFORE the node to be removed
        if cur.next:
            if self.tail == cur.next:
                self.tail = cur
            cur.next = cur.next.next 
            return True
        return False
        
    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        

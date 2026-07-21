# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        #move point to the node just before the left node
        for _ in range(left - 1):
            before = before.next
        current = before.next
        tail = current
        prev = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        before.next = prev
        tail.next = current
        return dummy.next
   
       
   






        
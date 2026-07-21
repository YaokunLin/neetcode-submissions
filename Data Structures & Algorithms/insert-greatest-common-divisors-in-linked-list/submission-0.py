# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a, b):
            while b != 0:
                remainder = a % b
                a = b
                b = remainder
            return a

        node, curr = head, head
        while curr.next:
            gcd = GCD(curr.val, curr.next.val)
          
            temp = curr.next
            curr.next = ListNode(gcd)
            curr.next.next = temp
            curr = temp
        return node
            



        
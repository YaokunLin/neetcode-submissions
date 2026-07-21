# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right = slow.next
        slow.next = None
        left = head
        prev_right = None
        # reverse the right half
        while right:
            temp = right.next
            right.next = prev_right
            prev_right = right
            right = temp
        # prev_right now is the reverse the half right
        # merge left and right
        while prev_right:
            temp1, temp2 = left.next, prev_right.next
            left.next = prev_right
            prev_right.next = temp1
            left = temp1
            prev_right = temp2
        



       
      
       

     
        



        
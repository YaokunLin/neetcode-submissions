# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid point of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head
        #reverse the right half
        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        #merge the left half and reversed right half
        while prev:
            temp1, temp2 = left.next, prev.next
            left.next = prev
            prev.next = temp1
            left = temp1
            prev = temp2


     

    
        



       
      
       

     
        



        
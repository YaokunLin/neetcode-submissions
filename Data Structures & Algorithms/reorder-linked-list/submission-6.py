# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid of linked list
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right = slow.next
        slow.next = None
        left = head
        # reverse the right half
        prev = None

        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        # merge left half and reversed right half
        reversed_right_head = prev
        while reversed_right_head:
            temp1 = left.next
            temp2 = reversed_right_head.next
            left.next = reversed_right_head
            reversed_right_head.next = temp1
            left = temp1
            reversed_right_head = temp2
        



  
    

           
        
       
       
     


     

    
        



       
      
       

     
        



        
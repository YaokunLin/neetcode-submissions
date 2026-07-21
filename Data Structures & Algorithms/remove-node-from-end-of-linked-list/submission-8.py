# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      #count the number of node in the linkedlist
      count = 0
      curr = head
      while curr:
        curr = curr.next
        count += 1

      pos_from_start = count - n + 1

      # remove the node from the linkedlist
      curr_list = head
      count_pos = 0
      res = dummy = ListNode()
      while curr_list:
        count_pos += 1
        if count_pos == pos_from_start:
            curr_list = curr_list.next
            continue
            
        dummy.next = curr_list
        dummy = dummy.next
        curr_list = curr_list.next
      dummy.next = None
      return res.next
    

        
        
        


   
        
  
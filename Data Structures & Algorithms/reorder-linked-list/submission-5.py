# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head_list = []
        cur = head
        while cur:
            head_list.append(cur)
            cur = cur.next
        n = len(head_list)
        l, r = 0, n - 1
        while l < r:
            head_list[l].next = head_list[r]
            l += 1
            if l == r:
                break
            head_list[r].next = head_list[l]
            r -= 1
        head_list[l].next = None
    

           
        
       
       
     


     

    
        



       
      
       

     
        



        
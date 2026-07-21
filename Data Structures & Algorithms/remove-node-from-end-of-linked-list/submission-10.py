# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next
        remove_i = total - n
        dummy = temp = ListNode(0)
        count = 0
        
        while head:
            if count == remove_i:
                temp.next = head.next
                if head.next:
                    head = head.next.next
                else:
                    head = None
            else:
                temp.next = head
                head = head.next
            temp = temp.next
            count += 1
        return dummy.next


 
        


        

 
    

        
        
        


   
        
  
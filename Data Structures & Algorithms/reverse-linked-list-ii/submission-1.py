# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse_arr = []
        curr = head
        count = 1
        while curr:
            if left <= count <= right:
                reverse_arr.append(curr.val)
            curr = curr.next
            count += 1
        dummy = temp = ListNode(0)
       

        i = 1
        c = 0
        reversed = reverse_arr[::-1]
        cur2 = head
        
        while cur2:
            if left <= i <= right:
                temp.next = ListNode(reversed[c])
                c += 1
                temp = temp.next
                cur2 = cur2.next
                i += 1
            
               
            else:
                temp.next = cur2
               
                temp = temp.next
                cur2 = cur2.next
                i += 1
                
        
        return dummy.next






        
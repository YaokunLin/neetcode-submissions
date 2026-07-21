# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get linked_list length
        curr = head
        linked_list_num = 0
        dummy = res = ListNode(0)  # Initialize dummy node with 0 and set res to point to dummy
        
        # Calculate the length of the linked list
        while curr:
            curr = curr.next
            linked_list_num += 1
        
        # Determine the position from the start (1-based index)
        start_n = linked_list_num - n + 1  # Convert to 1-based index
        
        # Remove the nth node from the end
        num = 0
        curr2 = head
        while curr2:
            num += 1
            if num == start_n:
                # Skip the nth node from the end
                dummy.next = curr2.next
            else:
                dummy.next = curr2
                dummy = dummy.next
            curr2 = curr2.next
        
        dummy.next = None  # Ensure the end of the list is properly terminated
        
        return res.next  # Return the new head of the list

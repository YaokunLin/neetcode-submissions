# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getVal(node, res):
            curr = node
            while curr:
                res.append(curr.val)
                curr = curr.next
            return res

        res1 = getVal(l1, [])
        res2 = getVal(l2, [])
        res1_sum = 0
        def getSum(arr, res_sum):
            for i, num in enumerate(arr):
                res_sum += num * 10**i
            return res_sum
        res1_sum = getSum(res1, 0)
        res2_sum = getSum(res2, 0)
        two_sum = res1_sum + res2_sum 
        res_arr = []
        if two_sum == 0:
            res_arr = [0]
        else:
            while two_sum != 0:
                remainder = two_sum % 10
                res_arr.append(remainder)
                left = two_sum // 10
                two_sum = left
        
        head = curr = ListNode(res_arr[0])
        for num in res_arr[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return head

        
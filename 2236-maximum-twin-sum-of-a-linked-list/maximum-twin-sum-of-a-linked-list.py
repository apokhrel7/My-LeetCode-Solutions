# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        prev = None

        # 1. Reverse first half of the linked list
        # 2. Find the middle of the linked list
        # 3. Expand outwards, check every pair from left side and right side, record max sum of left and right pairs
        
        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # By this time prev will be left side, slow will be on the right side
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            slow = slow.next
            prev = prev.next

        return res
        
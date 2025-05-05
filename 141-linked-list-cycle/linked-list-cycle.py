# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # use fast and slow pointer
        # slow pointer will move up one increment at a time
        # fast pointer will move double the amount
        # If there is a cycle, then fast pointer will meet with slow pointer
        # this is because if slow pointer is moving at increment s, then fast pointer is moving at 2s. in a cycle, 2s is same position as s

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
        
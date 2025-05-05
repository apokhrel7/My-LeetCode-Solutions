# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None
        while curr:
            next_node = curr.next  # make sure you save what the next node is, otherwise when iterating you will lose this when reversing the pointers

            # swap next with previous value to reverse the list
            curr.next = prev
            prev = curr  # save the current value as it will be the previous in next interation

            curr = next_node

        return prev

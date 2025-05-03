# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is empty, just return the datatype
        if not (head and head.next): return head

        prev = None
        current = head
        new_head = head.next 

        while current and current.next:
            second = current.next
            
            # swap if prev with second (next of current) exists
            if prev:
                prev.next = second

            # do the swapping
            current.next = second.next
            second.next = current

            # move pointers forward
            prev = current
            current = current.next

        return new_head
        
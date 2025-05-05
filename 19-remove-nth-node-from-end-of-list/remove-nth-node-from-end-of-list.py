# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        target = len(nodes) - n
        if target == 0: return head.next


        nodes[target - 1].next = nodes[target].next
        return nodes[0]
        

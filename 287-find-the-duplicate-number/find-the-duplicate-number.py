class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Same as Linked List Cyle II
        # Fast, slow, and extra node.
        # Find cycle, then use another node to find the head of that cycle

        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # now start the third pointer
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
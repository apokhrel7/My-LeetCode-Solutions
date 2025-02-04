class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # this problem is similar to driving a car and filling up gas whenever gas station is nearby

        max_jump = 0

        for num in nums:
            if max_jump < 0:
                return False
            elif num > max_jump:
                max_jump = num

            max_jump -= 1
        return True
        

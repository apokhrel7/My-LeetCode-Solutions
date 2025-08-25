class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curr_total = 0
        l = 0

        for i in range(len(arr)):
            curr_total += arr[i]

            # fixed window size reached, slide window to right
            if (i - l + 1) == k:
                if (curr_total / k) >= threshold:
                    count += 1
                    
                # Slide window
                curr_total -= arr[l]
                l += 1

        return count
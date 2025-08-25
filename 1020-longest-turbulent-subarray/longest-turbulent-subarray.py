class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l , r = 0, 1
        res, prev = 1, ""  # subarray length guaranteed to be at least 1

        while r < len(arr):
            # CASE: 1
            # if prev number > curr, and prev sign was not >,
            # increment right pointer and update prev 
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"

            # CASE 2:
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"

            # CASE 3: prev sign was the same or its "=" sign
            else:

                # if prev == curr number, then increment right pointer
                # as "=" sign is not valid
                if arr[r - 1] == arr[r]:
                    r += 1
                
                # here you increment left pointer as we're trying to find a new longest substring
                l = r - 1
                prev = ""  # this can be changed to "=" as well, doesn't matter

        return res
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time-complexity: O(n * m) where m is the given idle time (gap) but 0 <= m <= 100
        # Space-complexity : O(n)

        # first create counter to track number of occurances of each letter

        counter = {}
        for char in tasks:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        # heapify the occurances using max heap (Python only has MinHeap so reverse it)
        maxHeap = []
        for val in counter.values():
            heapq.heappush(maxHeap, -val)

        # create queue to determine which tasks can be completed
        q = deque()
        time = 0 

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))

            # as long as queue is not empty and we can finally complete the task after it has reached the proper interval, so add it to maxHeap 
            if q and q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])

        return time
        
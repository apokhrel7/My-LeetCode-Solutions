class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # use heap
        res = []

        minHeap = []

        
        for x, y in points:
            distance = (x**2 + y**2)**0.5
            minHeap.append([distance, [x, y]])

        heapq.heapify(minHeap)
        print(minHeap)

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
    
        return res


        

            


        
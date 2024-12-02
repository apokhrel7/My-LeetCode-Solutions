class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        self.dict[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # dict = {foo: [[bar1, 1], [bar2, 2]]}
        # binary search as all timestamps are given in ascending sorted order (as time moves only forwards)
        
        res = ""
        if key not in self.dict: return res

        l, r = 0, len(self.dict[key]) - 1

        array = self.dict[key]

        while l <= r:
            mid = (l + r) // 2

            if array[mid][1] <= timestamp:
                res = array[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return res

        


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
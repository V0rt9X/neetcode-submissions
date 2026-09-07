class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        
        self.cache[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        res = ""
        box = self.cache[key]

        l, r = 0, len(box) - 1

        while l <= r:
            mid = (l + r) // 2

            if box[mid][0] <= timestamp:
                res = box[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

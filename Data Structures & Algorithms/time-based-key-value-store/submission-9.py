class TimeMap:

    def __init__(self):
        self.Tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Tmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Tmap:
            return ""
        
        res = ""
        container = self.Tmap[key]
        
        l,r = 0, len(container) - 1
        while l<=r:
            mid = (l + r) // 2

            if container[mid][0] <= timestamp:
                l = mid + 1
                res = container[mid][1]
            else:
                r = mid - 1
        
        return res

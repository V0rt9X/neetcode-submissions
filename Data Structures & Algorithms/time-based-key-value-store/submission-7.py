class TimeMap:

    def __init__(self):
        self.Tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Tmap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        box = self.Tmap.get(key, [])
        l,r = 0, len(box) - 1
        res = ''

        while l<=r:
            mid = (l + r) // 2
            
            if box[mid][0] <= timestamp:
                res = box[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        


class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        container = self.cache[key]
        l, r = 0, len(container) - 1

        while l <= r:
            mid = (l + r) // 2

            if container[mid][0] <= timestamp:
                res = container[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        

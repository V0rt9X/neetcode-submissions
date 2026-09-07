class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            self.store[key].append((value, timestamp))
        else:
            self.store[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        container = self.store[key]
        l,r = 0, len(container) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            res = container[mid][0] if container[mid][1] <= timestamp else res

            if container[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
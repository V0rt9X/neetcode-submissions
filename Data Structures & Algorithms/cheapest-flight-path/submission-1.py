class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0


        for i in range(k + 1):
            tmpPrices = prices.copy()

            for dep, arr, cos in flights:
                if prices[dep] == float("inf"):
                    continue
                
                if prices[dep] + cos < tmpPrices[arr]:
                    tmpPrices[arr] = prices[dep] + cos
                
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1


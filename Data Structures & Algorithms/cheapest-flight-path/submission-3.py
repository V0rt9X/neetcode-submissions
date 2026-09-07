class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0


        for _ in range(k + 1):
            new_prices = prices.copy()
            for dep, arr, price in flights:
                if prices[dep] != float("inf"):
                    new_prices[arr] = min(new_prices[arr], prices[dep] + price)
            
            prices = new_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1

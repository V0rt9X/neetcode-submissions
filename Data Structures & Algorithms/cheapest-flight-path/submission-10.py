class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            new_prices = prices.copy()
            for s, d, price in flights:
                if prices[s] != float("inf"):
                    new_prices[d] = min(new_prices[d], prices[s] + price)
            
            prices = new_prices
        return prices[dst] if prices[dst] != float("inf") else -1
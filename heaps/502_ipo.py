class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit=[]
        min_capital=[(cap,profit) for cap,profit in zip(capital,profits)]
        heapq.heapify(min_capital)

        for idx in range(k):
            while min_capital and min_capital[0][0]<=w:
                cap,profit=heapq.heappop(min_capital)
                heapq.heappush(max_profit,-profit)
            if not max_profit:
                break
            w+= -heapq.heappop(max_profit)
        return w
        
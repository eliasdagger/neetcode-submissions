class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        # [2, 3, 3, 4, 4]
        while len(stones) > 1:
            print(stones)
        
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                z = -1 * abs(x - y)
                heapq.heappush(stones, z)
                
        return -1 * sum(stones)





        
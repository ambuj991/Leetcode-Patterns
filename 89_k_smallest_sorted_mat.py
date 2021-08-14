# k th smallest in sorted matrix
import heapq
class Solution:
    def kthSmallest( matrix, k) -> int:
        maxHeap = []
        for x in matrix:
            for y in x:
                if len(maxHeap) <k:
                    heapq.heappush(maxHeap, -y)
                else:
                    heapq.heappushpop(maxHeap, -y)
        return -maxHeap[0]

# O($n^2$logn) searc
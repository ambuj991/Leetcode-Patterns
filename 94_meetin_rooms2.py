import heapq
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        intervals=A
        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>=heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        return len(heap)
        
        # nlogn 